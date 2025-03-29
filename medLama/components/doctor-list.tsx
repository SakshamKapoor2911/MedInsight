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
              {doctor.telehealth && (
                <Video className="h-5 w-5 text-blue-500" />
              )}
            </CardTitle>
            <p className="text-sm text-muted-foreground">{doctor.specialty}</p>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              <p className="text-sm font-medium">Available Slots:</p>
              {doctor.availableSlots.map((slot) => (
                <Button
                  key={slot}
                  variant="outline"
                  className="w-full justify-start"
                  onClick={() => onSchedule(doctor, slot)}
                >
                  <Calendar className="mr-2 h-4 w-4" />
                  {new Date(slot).toLocaleString()}
                </Button>
              ))}
            </div>
          </CardContent>
          <CardFooter>
            {doctor.telehealth && (
              <p className="text-sm text-muted-foreground">
                ✓ Telehealth available
              </p>
            )}
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}