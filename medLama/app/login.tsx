
// Login page for MedLama frontend (local only)
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  // Form state
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  // Handle login form submit
  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    // Call local backend auth endpoint
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem("token", data.access_token);
      router.push("/");
    } else {
      setError("Invalid credentials");
    }
  }

  // Render login form
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <form onSubmit={handleLogin} className="bg-white p-8 rounded shadow w-80">
        <h2 className="text-2xl mb-4">Login</h2>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
          className="border p-2 mb-4 w-full"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          className="border p-2 mb-4 w-full"
        />
        {error && <div className="text-red-500 mb-2">{error}</div>}
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded w-full">Login</button>
        <a href="/register" className="text-blue-500 underline block mt-4">Register</a>
      </form>
    </div>
  );
}
