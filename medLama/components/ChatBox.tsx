import { useState } from "react";
import { useAuth } from "@/hooks/useAuth";

export default function ChatBox() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const { token } = useAuth();

  async function sendMessage() {
    setLoading(true);
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: JSON.stringify({ prompt: input }),
    });
    const data = await res.json();
    setMessages([...messages, `You: ${input}`, `AI: ${data.response}`]);
    setInput("");
    setLoading(false);
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
        <button onClick={sendMessage} disabled={loading} className="bg-blue-500 text-white px-4 py-2 rounded">
          Send
        </button>
      </div>
    </div>
  );
}
