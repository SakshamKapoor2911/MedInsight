import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Plus } from "lucide-react";
import type { SymptomSuggestion } from "@/lib/types";

interface SymptomSuggestionsProps {
  suggestions: SymptomSuggestion[];
  onSelect: (symptom: string) => void;
}

export function SymptomSuggestions({ suggestions, onSelect }: SymptomSuggestionsProps) {
  if (!suggestions.length) return null;

  return (
    <ScrollArea className="h-24">
      <div className="flex flex-wrap gap-2 p-2">
        {suggestions.map((suggestion) => (
          <Button
            key={suggestion.id}
            variant="outline"
            size="sm"
            className="rounded-full bg-secondary/50 hover:bg-secondary"
            onClick={() => onSelect(suggestion.name)}
          >
            <Plus className="mr-1 h-4 w-4" />
            {suggestion.name}
          </Button>
        ))}
      </div>
    </ScrollArea>
  );
}