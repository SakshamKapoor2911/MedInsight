"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Bot, Send, User, ArrowRight, Moon, Sun, Stethoscope } from "lucide-react";
import { SeverityIndicator } from "@/components/severity-indicator";
import { DoctorList } from "@/components/doctor-list";
import { EmergencyPanel } from "@/components/emergency-panel";
import { SymptomSuggestions } from "@/components/symptom-suggestions";
import { analyzeSymptoms, findAvailableDoctors } from "@/lib/analysis";
import { getEmergencyInfo } from "@/lib/emergency";
import { getSuggestedSymptoms } from "@/lib/symptoms";
import { useTheme } from "next-themes";
import type { SymptomAnalysis, DoctorMatch, SymptomSuggestion } from "@/lib/types";

interface Message {
  role: "user" | "assistant";
  content: string;
}

type Stage = "chat" | "analysis" | "doctors";

const LamaLogo = () => (
  <div className="relative group">
    <div className="absolute -inset-1 bg-gradient-to-r from-primary/20 to-green-500/20 rounded-full blur ai-thinking"></div>
    <div className="relative z-10 rounded-full bg-primary/10 p-2 transition-transform group-hover:scale-110">
      <div className="relative">
        <Bot className="h-6 w-6 text-primary" />
        <Stethoscope className="h-4 w-4 text-primary absolute -top-1 -right-1 transform rotate-45" />
      </div>
    </div>
  </div>
);

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Hello! I'm your AI health assistant powered by MedLama. Please describe what you're feeling in your own words. I'll guide you through it.",
    },
  ]);
  const [input, setInput] = useState("");
  const [stage, setStage] = useState<Stage>("chat");
  const [analysis, setAnalysis] = useState<SymptomAnalysis | null>(null);
  const [doctors, setDoctors] = useState<DoctorMatch[]>([]);
  const [isReadyForAnalysis, setIsReadyForAnalysis] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isDimmed, setIsDimmed] = useState(false);
  const [suggestions, setSuggestions] = useState<SymptomSuggestion[]>([]);
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    setIsDimmed(isProcessing);
  }, [isProcessing]);

  useEffect(() => {
    if (input.length > 2) {
      const newSuggestions = getSuggestedSymptoms(input);
      setSuggestions(newSuggestions);
    } else {
      setSuggestions([]);
    }
  }, [input]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: "user" as const, content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setSuggestions([]);
    setIsProcessing(true);

    const messageCount = messages.length;
    let aiResponse: Message;

    if (messageCount === 1) {
      aiResponse = {
        role: "assistant",
        content: "When did these symptoms start? And have they gotten worse over time?",
      };
    } else if (messageCount === 3) {
      aiResponse = {
        role: "assistant",
        content: "Do you have any medical history or conditions that might be relevant? Even if you don't think it's directly related, it's important to know.",
      };
    } else if (messageCount === 5) {
      aiResponse = {
        role: "assistant",
        content: "I think I have enough information to analyze your symptoms. Click 'Done' when you're ready for the analysis, or feel free to add any other details you think might be important.",
      };
      setIsReadyForAnalysis(true);
    } else {
      aiResponse = {
        role: "assistant",
        content: "Thank you for providing that information. Is there anything else you'd like to add?",
      };
    }

    setTimeout(() => {
      setMessages((prev) => [...prev, aiResponse]);
      setIsProcessing(false);
    }, 1000);
  };

  const handleAnalysis = async () => {
    setIsProcessing(true);
    const symptoms = messages
      .filter((msg) => msg.role === "user")
      .map((msg) => msg.content)
      .join(" ");

    const result = await analyzeSymptoms(symptoms);
    
    if (result.severity === "high") {
      const emergencyInfo = await getEmergencyInfo("current-location");
      result.emergencyInfo = emergencyInfo;
    }
    
    setAnalysis(result);
    const availableDoctors = await findAvailableDoctors(result.suggestedSpecialists[0]);
    setDoctors(availableDoctors);
    setStage("analysis");
    setIsProcessing(false);
  };

  const handleSuggestionSelect = (symptom: string) => {
    setInput((prev) => prev + (prev ? `, ${symptom}` : symptom));
  };

  const handleEmergencyCall = () => {
    // In a real app, this would integrate with the device's phone system
    window.location.href = "tel:911";
  };

  const Header = () => (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between">
        <div className="flex items-center gap-3">
          <LamaLogo />
          <div>
            <span className="text-xl font-semibold bg-gradient-to-r from-primary via-green-500 to-emerald-500 bg-clip-text text-transparent">
              MedLama
            </span>
            <span className="text-xs text-muted-foreground block">AI-Powered Health Assistant</span>
          </div>
        </div>
        <Button
          variant="ghost"
          size="icon"
          onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
          className="rounded-full hover:bg-secondary/80"
        >
          {theme === "dark" ? (
            <Sun className="h-5 w-5" />
          ) : (
            <Moon className="h-5 w-5" />
          )}
        </Button>
      </div>
    </header>
  );

  if (stage === "analysis" && analysis) {
    return (
      <div className="flex min-h-screen flex-col bg-background hexagon-bg">
        <Header />
        <main className="flex flex-1 flex-col items-center p-4 md:p-8">
          <Card className="w-full max-w-4xl p-6 shadow-lg glass-card">
            <h2 className="text-2xl font-bold mb-6 bg-gradient-to-r from-primary to-green-600 bg-clip-text text-transparent">
              Symptom Analysis
            </h2>
            <SeverityIndicator severity={analysis.severity} />
            
            {analysis.severity === "high" && analysis.emergencyInfo && (
              <div className="mt-6">
                <EmergencyPanel 
                  info={analysis.emergencyInfo} 
                  onCallEmergency={handleEmergencyCall} 
                />
              </div>
            )}

            <div className="mt-8">
              <h3 className="text-xl font-semibold mb-4">Recommendations</h3>
              <ul className="space-y-3">
                {analysis.recommendations.map((rec, i) => (
                  <li key={i} className="flex items-center text-muted-foreground">
                    <span className="mr-3 text-primary">•</span>
                    {rec}
                  </li>
                ))}
              </ul>
            </div>

            <div className="mt-8">
              <h3 className="text-xl font-semibold mb-4">Available Specialists</h3>
              <DoctorList doctors={doctors} onSchedule={() => {}} />
            </div>

            <Button 
              className="mt-8"
              onClick={() => setStage("chat")}
              variant="outline"
            >
              Start New Consultation
            </Button>
          </Card>
        </main>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col bg-background hexagon-bg">
      <Header />
      <main className="flex flex-1 flex-col items-center p-4 md:p-8">
        <Card className={`flex h-[80vh] w-full max-w-4xl flex-col shadow-lg glass-card transition-opacity duration-300 ${isDimmed ? 'opacity-95' : ''}`}>
          <ScrollArea className="flex-1 p-4 chat-container">
            <div className="space-y-4">
              {messages.map((message, i) => (
                <div
                  key={i}
                  className={`flex items-start gap-4 message-fade-in ${
                    message.role === "assistant" ? "flex-row" : "flex-row-reverse"
                  }`}
                >
                  <div className={`rounded-full p-2 ${
                    message.role === "assistant" 
                      ? "bg-primary/10" 
                      : "bg-secondary"
                  }`}>
                    {message.role === "assistant" ? (
                      <Bot className="h-6 w-6 text-primary" />
                    ) : (
                      <User className="h-6 w-6" />
                    )}
                  </div>
                  <div
                    className={`rounded-lg px-4 py-3 ${
                      message.role === "assistant"
                        ? "bg-card/50 border shadow-sm backdrop-blur-sm"
                        : "bg-primary text-primary-foreground"
                    }`}
                  >
                    {message.content}
                  </div>
                </div>
              ))}
              {isProcessing && (
                <div className="flex items-center gap-2 text-muted-foreground processing">
                  <Bot className="h-5 w-5" />
                  <span>Analyzing...</span>
                </div>
              )}
            </div>
          </ScrollArea>

          <div className="border-t p-4 space-y-4 bg-background/50 backdrop-blur-sm">
            {suggestions.length > 0 && (
              <SymptomSuggestions 
                suggestions={suggestions} 
                onSelect={handleSuggestionSelect} 
              />
            )}
            
            <form
              onSubmit={handleSubmit}
              className="flex items-center gap-2"
            >
              <Input
                placeholder="Describe what you're feeling..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                className="flex-1 rounded-full bg-secondary/50"
              />
              <Button 
                type="submit" 
                size="icon" 
                className="rounded-full hover:glow-effect"
                disabled={isProcessing}
              >
                <Send className="h-4 w-4" />
              </Button>
            </form>

            {isReadyForAnalysis && (
              <Button 
                className="w-full rounded-full hover:glow-effect"
                onClick={handleAnalysis}
                variant="default"
                disabled={isProcessing}
              >
                {isProcessing ? (
                  <span className="flex items-center gap-2">
                    <Bot className="h-4 w-4 animate-spin" />
                    Analyzing Symptoms...
                  </span>
                ) : (
                  <>
                    Done - Analyze Symptoms
                    <ArrowRight className="ml-2 h-4 w-4" />
                  </>
                )}
              </Button>
            )}
          </div>
        </Card>
      </main>
    </div>
  );
}