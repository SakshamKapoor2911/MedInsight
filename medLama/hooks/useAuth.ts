import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export function useAuth() {
  const [token, setToken] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    const t = localStorage.getItem("token");
    setToken(t);
    if (!t) {
      router.push("/login");
    }
  }, [router]);

  function logout() {
    localStorage.removeItem("token");
    setToken(null);
    router.push("/login");
  }

  return { token, logout };
}
