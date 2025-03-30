import type { SymptomSuggestion } from "./types";

export const commonSymptoms: SymptomSuggestion[] = [
  {
    id: "headache",
    name: "Headache",
    category: "Neurological",
    relatedSymptoms: ["Migraine", "Tension headache", "Sinus pressure"],
    bodyPart: "Head"
  },
  {
    id: "chest-pain",
    name: "Chest Pain",
    category: "Cardiovascular",
    relatedSymptoms: ["Shortness of breath", "Heart palpitations", "Chest tightness"],
    bodyPart: "Chest"
  },
  {
    id: "fever",
    name: "Fever",
    category: "General",
    relatedSymptoms: ["Chills", "Body aches", "Fatigue"],
  },
  {
    id: "cough",
    name: "Cough",
    category: "Respiratory",
    relatedSymptoms: ["Dry cough", "Wet cough", "Wheezing"],
    bodyPart: "Chest"
  }
];

export function getSuggestedSymptoms(input: string): SymptomSuggestion[] {
  const searchTerms = input.toLowerCase().split(' ');
  
  return commonSymptoms.filter(symptom => {
    const matchesName = searchTerms.some(term => 
      symptom.name.toLowerCase().includes(term) ||
      symptom.category.toLowerCase().includes(term) ||
      symptom.relatedSymptoms.some(s => s.toLowerCase().includes(term))
    );
    return matchesName;
  });
}