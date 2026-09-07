"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { Shell, Conversations, Messages } from "../components";
import { useApp } from "../providers";

type GraphRun = { run_id: string; state: Record<string, unknown>; tool_calls: { tool_name: string; status: string; input: unknown; output: unknown }[] };
const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export default function Debug(){
  const {convs,selected}=useApp(); const params=useSearchParams(); const runId=params.get("run");
  const [run,setRun]=useState<GraphRun|null>(null); const c=convs.find(x=>x.id===selected);
  useEffect(()=>{if(!runId){setRun(null);return;} fetch(`${apiUrl}/api/runs/${runId}`).then(response=>response.ok?response.json():null).then(setRun).catch(()=>setRun(null));},[runId]);
  const state=run?.state??c?.state??{conversation_id:c?.id};
  return <Shell><main className="chat-layout"><Conversations/><section className="debug"><header><p className="eyebrow">Trace inspector</p><h1>{run?`Reply run ${run.run_id.slice(0,8)}`:c?.title}</h1><span>{run?"Durable graph snapshot and tool evidence":"Select an agent reply to inspect its saved run."}</span></header><div className="debug-grid"><div className="panel"><h2>Conversation</h2>{c&&<Messages conversation={c}/>}</div><div className="panel"><h2>Agent trace</h2>{run?.tool_calls.map((tool,i)=><div className="trace" key={i}><span>●</span><div><b>{tool.tool_name}</b><p>{tool.status}</p><code>{JSON.stringify({input:tool.input,output:tool.output}).slice(0,360)}</code></div><small>complete</small></div>)??c?.trace.map((t,i)=><div className="trace" key={i}><span>●</span><div><b>{t.agent}</b><p>{t.detail}</p>{t.tool&&<code>{t.tool}</code>}</div><small>complete</small></div>)}<h2>State</h2><pre>{JSON.stringify(state,null,2)}</pre></div></div></section></main></Shell>
}
