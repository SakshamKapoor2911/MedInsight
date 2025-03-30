import { StaticImageData } from 'next/image';

export interface Message {
  role: "user" | "assistant";
  content: string;
  suggestions?: string[];
}

export interface SymptomAnalysis {
  severity: "low" | "moderate" | "high";
  recommendations: string[];
  suggestedSpecialists: string[];
  medicalChart?: MedicalChart;
  emergencyInfo?: EmergencyInfo;
}

export interface DoctorMatch {
  name: string;
  email: string;
  phone: string;
  specialty: string;
  address: string;
}

export interface MedicalChart {
  chiefComplaint: string;
  historyOfPresentIllness: string;
  pastMedicalHistory: string;
  medications: string[];
  allergies: string[];
  vitalSigns?: {
    temperature?: string;
    bloodPressure?: string;
    heartRate?: string;
    respiratoryRate?: string;
  };
  assessment: string;
  plan: string;
  followUpInstructions: string;
}

export interface EmergencyInfo {
  nearbyFacilities: EmergencyFacility[];
  emergencyContacts: EmergencyContact[];
  firstAidSteps?: string[];
}

export interface EmergencyFacility {
  name: string;
  type: "hospital" | "urgentCare" | "clinic";
  distance: string;
  address: string;
  phone: string;
  waitTime?: string;
  openNow: boolean;
}

export interface EmergencyContact {
  name: string;
  relationship: string;
  phone: string;
  isICE: boolean;
}

export interface SymptomSuggestion {
  id: string;
  name: string;
  category: string;
  relatedSymptoms: string[];
  bodyPart?: string;
}