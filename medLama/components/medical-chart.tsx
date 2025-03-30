// import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
// import { Separator } from "@/components/ui/separator";
// import type { MedicalChart } from "@/lib/types";

// interface MedicalChartProps {
//   chart: MedicalChart;
// }

// export function MedicalChart({ chart }: MedicalChartProps) {
//   return (
//     <Card className="w-full">
//       <CardHeader>
//         <CardTitle>Medical Chart</CardTitle>
//       </CardHeader>
//       <CardContent className="space-y-4">
//         <div>
//           <h3 className="font-semibold">Chief Complaint</h3>
//           <p className="text-muted-foreground">{chart.chiefComplaint}</p>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">History of Present Illness</h3>
//           <p className="text-muted-foreground">{chart.historyOfPresentIllness}</p>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Past Medical History</h3>
//           <p className="text-muted-foreground">
//             {chart.pastMedicalHistory || "No past medical history provided"}
//           </p>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Medications</h3>
//           <ul className="list-disc list-inside text-muted-foreground">
//             {chart.medications.length > 0 ? (
//               chart.medications.map((med, i) => <li key={i}>{med}</li>)
//             ) : (
//               <li>No current medications</li>
//             )}
//           </ul>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Allergies</h3>
//           <ul className="list-disc list-inside text-muted-foreground">
//             {chart.allergies.length > 0 ? (
//               chart.allergies.map((allergy, i) => <li key={i}>{allergy}</li>)
//             ) : (
//               <li>No known allergies</li>
//             )}
//           </ul>
//         </div>
//         {chart.vitalSigns && (
//           <>
//             <Separator />
//             <div>
//               <h3 className="font-semibold">Vital Signs</h3>
//               <div className="grid grid-cols-2 gap-2 text-muted-foreground">
//                 {Object.entries(chart.vitalSigns).map(([key, value]) => (
//                   <div key={key}>
//                     <span className="font-medium">{key}: </span>
//                     {value}
//                   </div>
//                 ))}
//               </div>
//             </div>
//           </>
//         )}
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Assessment</h3>
//           <p className="text-muted-foreground">{chart.assessment}</p>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Plan</h3>
//           <p className="text-muted-foreground">{chart.plan}</p>
//         </div>
//         <Separator />
//         <div>
//           <h3 className="font-semibold">Follow-up Instructions</h3>
//           <p className="text-muted-foreground">{chart.followUpInstructions}</p>
//         </div>
//       </CardContent>
//     </Card>
//   );
// }