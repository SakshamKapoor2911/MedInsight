import { SymptomAnalysis, DoctorMatch, MedicalChart } from "./types";

interface SymptomPattern {
  keywords: string[];
  severity: "low" | "moderate" | "high";
  condition: string;
  recommendations: string[];
  specialists: string[];
  urgency: string;
  followUp: string;
  medications?: string[];
  tests?: string[];
}

const symptomPatterns: SymptomPattern[] = [
  {
    keywords: ["chest pain", "chest tightness", "difficulty breathing", "shortness of breath"],
    severity: "high",
    condition: "Possible Cardiac Event",
    recommendations: [
      "Seek immediate emergency care",
      "Call emergency services (911)",
      "Stop any physical activity",
      "Sit or lie down and try to stay calm",
      "If prescribed, take nitroglycerin as directed"
    ],
    specialists: ["Cardiologist", "Emergency Medicine"],
    urgency: "Immediate emergency care required",
    followUp: "Schedule follow-up with cardiologist after emergency evaluation",
    tests: [
      "ECG/EKG",
      "Cardiac enzymes",
      "Chest X-ray",
      "Blood pressure monitoring"
    ]
  },
  {
    keywords: ["severe headache", "worst headache", "sudden headache", "vision changes", "confusion"],
    severity: "high",
    condition: "Possible Neurological Emergency",
    recommendations: [
      "Seek immediate medical attention",
      "Do not drive yourself",
      "Note time of symptom onset",
      "Avoid taking blood thinners"
    ],
    specialists: ["Neurologist", "Emergency Medicine"],
    urgency: "Emergency evaluation needed",
    followUp: "Neurological follow-up within 48 hours",
    tests: [
      "CT scan",
      "MRI",
      "Neurological examination"
    ]
  },
  {
    keywords: ["fever", "cough", "sore throat", "body aches"],
    severity: "moderate",
    condition: "Possible Upper Respiratory Infection",
    recommendations: [
      "Rest and stay hydrated",
      "Monitor temperature every 4 hours",
      "Use over-the-counter fever reducers if needed",
      "Isolate to prevent spread",
      "Watch for worsening symptoms"
    ],
    specialists: ["Primary Care Physician", "Internal Medicine"],
    urgency: "Schedule appointment within 24-48 hours",
    followUp: "Follow up if symptoms persist beyond 5 days",
    medications: [
      "Acetaminophen",
      "Ibuprofen",
      "Throat lozenges",
      "Cough suppressants"
    ]
  },
  {
    keywords: ["rash", "itching", "hives"],
    severity: "moderate",
    condition: "Possible Allergic Reaction",
    recommendations: [
      "Take antihistamine if available",
      "Avoid potential triggers",
      "Apply cool compress",
      "Monitor for breathing difficulties"
    ],
    specialists: ["Allergist", "Dermatologist"],
    urgency: "Schedule appointment within 48 hours",
    followUp: "Follow up if symptoms worsen or persist",
    medications: [
      "Oral antihistamines",
      "Topical cortisone",
      "Calamine lotion"
    ]
  }
];

function matchSymptomPattern(symptoms: string): SymptomPattern {
  const normalizedSymptoms = symptoms.toLowerCase();

  // Check for emergency keywords first
  const emergencyPattern = symptomPatterns.find(pattern =>
    pattern.severity === "high" && pattern.keywords.some(keyword =>
      normalizedSymptoms.includes(keyword)
    )
  );

  if (emergencyPattern) return emergencyPattern;

  // Check for moderate severity patterns
  const moderatePattern = symptomPatterns.find(pattern =>
    pattern.severity === "moderate" && pattern.keywords.some(keyword =>
      normalizedSymptoms.includes(keyword)
    )
  );

  if (moderatePattern) return moderatePattern;

  // Default pattern for unmatched symptoms
  return {
    keywords: [],
    severity: "low",
    condition: "Non-specific Symptoms",
    recommendations: [
      "Monitor symptoms",
      "Rest and maintain good hydration",
      "Over-the-counter remedies may help",
      "Keep a symptom diary"
    ],
    specialists: ["Primary Care Physician"],
    urgency: "Schedule routine appointment if symptoms persist",
    followUp: "Follow up if symptoms worsen or don't improve within a week"
  };
}

function generateMedicalChart(symptoms: string, pattern: SymptomPattern): MedicalChart {
  return {
    chiefComplaint: pattern.condition,
    historyOfPresentIllness: symptoms,
    pastMedicalHistory: "",
    medications: pattern.medications || [],
    allergies: [],
    vitalSigns: {
      temperature: "To be measured",
      bloodPressure: "To be measured",
      heartRate: "To be measured",
      respiratoryRate: "To be measured"
    },
    assessment: `${pattern.condition}. Severity: ${pattern.severity}. ${pattern.urgency}`,
    plan: pattern.recommendations.join(". ") +
          (pattern.tests ? `. Recommended tests: ${pattern.tests.join(", ")}` : ""),
    followUpInstructions: pattern.followUp
  };
}

export async function analyzeSymptoms(symptoms: string): Promise<SymptomAnalysis> {
  const pattern = matchSymptomPattern(symptoms);

  return {
    severity: pattern.severity,
    recommendations: pattern.recommendations,
    suggestedSpecialists: pattern.specialists,
    medicalChart: generateMedicalChart(symptoms, pattern)
  };
}

export async function findAvailableDoctors(specialty: string, latitude: number = 38.02931000, longitude: number = -78.47668000): Promise<DoctorMatch[]> {
  console.log(specialty);

  try {
    const res = await fetch(`http://127.0.0.1:5000/api/doctors?latitude=${latitude}&longitude=${longitude}&specialty=${specialty}`);
    return await res.json();
  } catch (err) {
    console.log(err);
  }

  return [];
}