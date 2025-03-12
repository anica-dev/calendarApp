import React from "react";
import FullCalendar from "@fullcalendar/react";
import dayGridPlugin from "@fullcalendar/daygrid";

export default function MyCalendar() {
  return (
    <div style={{ width: "80%", margin: "auto" }}>
      <FullCalendar
        plugins={[dayGridPlugin]}
        initialView="dayGridMonth"
        events={[
          { title: "Tech Conference", date: "2025-03-10", description: "Tech talks & networking" },
          { title: "Startup Meetup", date: "2025-03-15", description: "Pitching and discussions" },
        ]}
        height="600px" // Adjust the height to make cells larger
      />
    </div>
  );
}
