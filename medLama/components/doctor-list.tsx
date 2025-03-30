import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card";
import { Calendar, Video } from "lucide-react";
import type { DoctorMatch } from "@/lib/types";

interface DoctorListProps {
  doctors: DoctorMatch[];
  onSchedule: (doctor: DoctorMatch, slot: string) => void;
}

export function DoctorList({ doctors, onSchedule }: DoctorListProps) {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {doctors.map((doctor) => (
        <Card key={doctor.name}>
          <CardHeader>
            <CardTitle className="flex items-center justify-between">
              <span>{doctor.name}</span>
            </CardTitle>
            <p className="text-sm text-muted-foreground">{doctor.specialty}</p>
          </CardHeader>
          <CardContent>
            <p className="text-muted-foreground">Email: {doctor.email}</p>
            <p className="text-muted-foreground">Phone: {doctor.phone}</p>
          </CardContent>
          <CardFooter>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}