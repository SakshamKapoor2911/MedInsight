import { useEffect, useRef, useState } from "react";
import { useAuth } from "@/hooks/useAuth";

export default function RealtimeChat() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");
  const ws = useRef<WebSocket | null>(null);
  const { token } = useAuth();

  useEffect(() => {
    if (!token) return;
    ws.current = new WebSocket(`ws://localhost:8080/ws?token=${token}`);
    ws.current.onmessage = (event) => {
      setMessages((prev) => [...prev, event.data]);
    };
    return () => {
      ws.current?.close();
    };
  }, [token]);

  function sendMessage() {
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      ws.current.send(input);
      setInput("");
    }
  }

  return (
    <div>
      <div className="mb-4">
        {messages.map((msg, i) => (
          <div key={i}>{msg}</div>
        ))}
      </div>
      <div>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          className="border p-2 mr-2"
        />
        <button onClick={sendMessage} className="bg-green-500 text-white px-4 py-2 rounded">
          Send (Realtime)
        </button>
      </div>
    </div>
  );
}
