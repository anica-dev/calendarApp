import React, { useEffect, useState } from "react";

const Events = () => {
    const [events, setEvents] = useState([]);  // Events start as an empty array

    useEffect(() => {
        fetch("http://127.0.0.1:8000/scrape/")  // Fetch events from Django API
            .then(response => response.json())
            .then(data => setEvents(data))
            .catch(error => console.error("Error fetching events:", error));
    }, []);

    return (
        <div>
            <h3>Upcoming Events</h3>
            <ul>
                {events.map((event) => (
                    <li key={event.id}>
                        {event.title}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Events;
