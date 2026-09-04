"use client";
import { useEffect, useState } from "react";
export default function Home() { const [status,setStatus]=useState("Checking backend…"); useEffect(()=>{fetch(`${process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000"}/health/ready`).then(r=>setStatus(r.ok?"Backend and database are ready":"Backend is unavailable")).catch(()=>setStatus("Backend is unavailable"));},[]); return <main><p>PHASE 1 · FOUNDATION</p><h1>Cato AI Support Engineer</h1><p>Customer chat and reviewer console will be added in later phases.</p><strong>{status}</strong></main>; }
