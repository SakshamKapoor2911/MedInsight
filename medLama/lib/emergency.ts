import type { EmergencyInfo, EmergencyFacility } from "./types";

export async function getEmergencyInfo(location: string): Promise<EmergencyInfo> {
  // This would typically call an API to get real emergency facility data
  // For demo purposes, we're returning mock data
  const mockFacilities: EmergencyFacility[] = [
    {
      name: "City General Hospital",
      type: "hospital",
      distance: "2.3 miles",
      address: "123 Medical Center Dr",
      phone: "(555) 123-4567",
      waitTime: "15 minutes",
      openNow: true
    },
    {
      name: "Urgent Care Plus",
      type: "urgentCare",
      distance: "1.1 miles",
      address: "456 Health Ave",
      phone: "(555) 987-6543",
      waitTime: "30 minutes",
      openNow: true
    }
  ];

  return {
    nearbyFacilities: mockFacilities,
    emergencyContacts: [
      {
        name: "John Doe",
        relationship: "Spouse",
        phone: "(555) 111-2222",
        isICE: true
      }
    ],
    firstAidSteps: [
      "Stay calm and assess the situation",
      "If experiencing chest pain, sit down and rest",
      "Take any prescribed emergency medication",
      "Stay on the line with emergency services"
    ]
  };
}