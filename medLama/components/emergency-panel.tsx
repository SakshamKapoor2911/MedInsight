import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Phone, Clock, MapPin, AlertTriangle } from "lucide-react";
// import type { EmergencyInfo } from "@/lib/types";

// interface EmergencyPanelProps {
//   info: EmergencyInfo;
//   onCallEmergency: () => void;
// }

// export function EmergencyPanel({ info, onCallEmergency }: EmergencyPanelProps) {
//   return (
//     <div className="space-y-4">
//       <Button
//         variant="destructive"
//         className="w-full text-lg font-semibold py-6 animate-pulse"
//         onClick={onCallEmergency}
//       >
//         <Phone className="mr-2 h-5 w-5" />
//         Call Emergency Services (911)
//       </Button>
//
//       <div className="grid gap-4 md:grid-cols-2">
//         {info.nearbyFacilities.map((facility) => (
//           <Card key={facility.name} className="relative overflow-hidden">
//             {facility.openNow && (
//               <Badge
//                 variant="secondary"
//                 className="absolute top-2 right-2"
//               >
//                 Open Now
//               </Badge>
//             )}
//             <CardHeader>
//               <CardTitle className="flex items-center justify-between">
//                 <span>{facility.name}</span>
//                 <Badge variant={facility.type === "hospital" ? "destructive" : "outline"}>
//                   {facility.type}
//                 </Badge>
//               </CardTitle>
//             </CardHeader>
//             <CardContent>
//               <div className="space-y-2 text-sm">
//                 <div className="flex items-center text-muted-foreground">
//                   <MapPin className="mr-2 h-4 w-4" />
//                   {facility.address}
//                 </div>
//                 <div className="flex items-center text-muted-foreground">
//                   <Clock className="mr-2 h-4 w-4" />
//                   {facility.waitTime ? `Wait time: ${facility.waitTime}` : 'Wait time unavailable'}
//                 </div>
//                 <div className="flex items-center text-muted-foreground">
//                   <Phone className="mr-2 h-4 w-4" />
//                   {facility.phone}
//                 </div>
//                 <Button
//                   variant="outline"
//                   className="w-full mt-2"
//                   onClick={() => window.open(`https://maps.google.com/?q=${encodeURIComponent(facility.address)}`, '_blank')}
//                 >
//                   Get Directions
//                 </Button>
//               </div>
//             </CardContent>
//           </Card>
//         ))}
//       </div>
//
//       {info.firstAidSteps && (
//         <Card>
//           <CardHeader>
//             <CardTitle className="flex items-center">
//               <AlertTriangle className="mr-2 h-5 w-5 text-destructive" />
//               Immediate First Aid Steps
//             </CardTitle>
//           </CardHeader>
//           <CardContent>
//             <ol className="list-decimal list-inside space-y-2">
//               {info.firstAidSteps.map((step, index) => (
//                 <li key={index} className="text-muted-foreground">{step}</li>
//               ))}
//             </ol>
//           </CardContent>
//         </Card>
//       )}
//     </div>
//   );
// }