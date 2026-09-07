"use client";

import { createContext, useContext, useEffect, useState } from "react";

const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
type Citation = { evidence_id: string; source: string; fact: string };
type ApiMessage = { message_id: string; role: "customer" | "agent"; content: string; created_at: string; citations: Citation[]; run_id: string | null };
type ApiConversation = { conversation_id: string; customer_id: string; requester_email: string; title: string; messages: ApiMessage[] };
type ApiApproval = { approval_id: string; customer_id: string; action_type: string; reason: string; status: "pending" | "approved" | "rejected" };
type ApiAlert = { alert_id: string; customer_id: string; severity: string; kind: string; summary: string; status: string };
export type Msg = { role: "customer" | "agent"; text: string; time: string; citations?: Citation[]; runId?: string; pending?: boolean };
export type Conv = { id: string; title: string; customer: string; site: string; status: string; messages: Msg[]; trace: { agent: string; detail: string; tool?: string }[]; state?: Record<string, unknown> };
export type Task = { id: string; kind: string; title: string; customer: string; detail: string; status: "open" | "approved" | "rejected" };

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${apiUrl}${path}`, { headers: { "Content-Type": "application/json" }, ...options });
  if (!response.ok) throw new Error((await response.json().catch(() => null))?.detail ?? "Request failed");
  return response.status === 204 ? (undefined as T) : response.json() as Promise<T>;
}
function traceFromState(state: Record<string, unknown> = {}): Conv["trace"] {
  return [["triage_result", "Triage"], ["diagnostic_evidence", "Diagnostics"], ["knowledge_evidence", "Knowledge"], ["action_result", "Action"]].flatMap(([key, agent]) => {
    const value = state[key] as Record<string, unknown> | undefined;
    const tool = key === "diagnostic_evidence" ? "get_client_diagnostics" : key === "knowledge_evidence" ? "search_knowledge_base" : undefined;
    return value ? [{ agent, detail: String(value.status ?? value.route ?? value.action ?? "complete"), tool }] : [];
  });
}
function toConversation(value: ApiConversation, state: Record<string, unknown> = {}, freshCitations: Citation[] = []): Conv {
  const action = state.action_result as Record<string, unknown> | undefined;
  return {
    id: value.conversation_id, title: value.title, customer: value.requester_email, site: "Customer account",
    status: action?.action === "approval_request" ? "Waiting for review" : "Active",
    messages: value.messages.map((message, index) => ({
      role: message.role, text: message.content,
      time: new Date(message.created_at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      citations: message.citations.length ? message.citations : message.role === "agent" && index === value.messages.length - 1 ? freshCitations : undefined, runId: message.run_id ?? undefined,
    })), trace: traceFromState(state), state,
  };
}
type Store = { convs: Conv[]; selected: string; tasks: Task[]; error: string | null; isSending: boolean; isReplying: boolean; select: (id: string) => void; add: () => Promise<void>; remove: (id: string) => Promise<void>; send: (text: string) => Promise<void>; resolve: (id: string, status: "approved" | "rejected" | "edit") => Promise<void> };
const C = createContext<Store | null>(null);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [convs, setConvs] = useState<Conv[]>([]); const [selected, setSelected] = useState("");
  const [tasks, setTasks] = useState<Task[]>([]); const [error, setError] = useState<string | null>(null); const [sendingConversationId, setSendingConversationId] = useState<string | null>(null);
  const isSending = sendingConversationId !== null; const isReplying = sendingConversationId === selected;
  useEffect(() => { Promise.all([request<ApiApproval[]>("/api/approvals"),request<ApiAlert[]>("/api/alerts")]).then(([approvals,alerts]) => setTasks([...approvals.map(item => ({ id: item.approval_id, kind: "Human approval", title: item.action_type.replaceAll("_", " "), customer: item.customer_id, detail: item.reason, status: item.status === "pending" ? "open" : item.status })),...alerts.map(item=>({id:item.alert_id,kind:"Sev-1 escalation",title:item.severity,customer:item.customer_id,detail:item.summary,status:"open" as const}))])).catch(() => undefined); }, []);
  useEffect(() => { const requesterEmail = window.localStorage.getItem("requester_email"); if (requesterEmail) request<ApiConversation[]>(`/api/conversations?requester_email=${encodeURIComponent(requesterEmail)}`).then(items => { const loaded = items.map(item => toConversation(item)); setConvs(loaded); setSelected(loaded[0]?.id ?? ""); }).catch(() => undefined); }, []);
  const add = async () => { const requesterEmail = window.prompt("Requester email (must use a known account domain):"); if (!requesterEmail) return; try { const created = await request<ApiConversation>("/api/conversations", { method: "POST", body: JSON.stringify({ requester_email: requesterEmail }) }); const conversation = toConversation(created); window.localStorage.setItem("requester_email", requesterEmail); setConvs(current => [conversation, ...current]); setSelected(conversation.id); setError(null); } catch (cause) { setError(cause instanceof Error ? cause.message : "Could not create conversation"); } };
  const remove = async (id: string) => { try { await request<void>(`/api/conversations/${id}`, { method: "DELETE" }); setConvs(current => { const next = current.filter(item => item.id !== id); if (selected === id) setSelected(next[0]?.id ?? ""); return next; }); } catch (cause) { setError(cause instanceof Error ? cause.message : "Could not delete conversation"); } };
  const send = async (text: string) => {
    if (!selected || sendingConversationId) return;
    const conversationId = selected;
    const optimisticMessage: Msg = { role: "customer", text, time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }), pending: true };
    setConvs(current => current.map(item => item.id === conversationId ? { ...item, messages: [...item.messages, optimisticMessage] } : item));
    setSendingConversationId(conversationId); setError(null);
    try {
      const turn = await request<{ conversation: ApiConversation; state: Record<string, unknown>; response: { citations?: Citation[] } }>(`/api/conversations/${conversationId}/messages`, { method: "POST", body: JSON.stringify({ content: text }) });
      const conversation = toConversation(turn.conversation, turn.state, turn.response.citations);
      setConvs(current => current.map(item => item.id === conversationId ? conversation : item));
    } catch (cause) { setConvs(current => current.map(item => item.id === conversationId ? { ...item, messages: item.messages.filter(message => message !== optimisticMessage) } : item)); setError(cause instanceof Error ? cause.message : "Could not send message"); }
    finally { setSendingConversationId(current => current === conversationId ? null : current); }
  };
  const resolve = async (id: string, status: "approved" | "rejected" | "edit") => { try { const note=status==="edit"?window.prompt("Reviewer edit note:")??"":undefined; await request<ApiApproval>(`/api/approvals/${id}/decision`, { method: "POST", body: JSON.stringify({ decision: status, reviewer: "demo-reviewer@local", note }) }); setTasks(current => current.map(item => item.id === id ? { ...item, status: status === "edit" ? "open" : status } : item)); } catch (cause) { setError(cause instanceof Error ? cause.message : "Could not decide approval"); } };
  return <C.Provider value={{ convs, selected, tasks, error, isSending, isReplying, select: setSelected, add, remove, send, resolve }}>{children}</C.Provider>;
}
export const useApp = () => { const value = useContext(C); if (!value) throw Error("missing provider"); return value; };
