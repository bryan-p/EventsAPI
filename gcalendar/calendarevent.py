class CalendarEvent:
    calendar_id = "primary"
    
    def create_event(self, event_body, notify=False):
        """
            Needed fields:
                summary, start, end, desc, location, recurrence
        """
        event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        return event['id']

    def delete_event(eventt_id, notify=False):
        service.events().delete(calendarId=calendar_id, eventId=event_id, sendNotifications=notify)

    def delete_events(event_id_list, notify=False):
        for eventt_id in event_id_list:
            service.events().delete(calendarId=calendar_id, eventId=event_id, sendNotifications=notify)

    def update_event(self, event_id, event_body, notify=False):
        return service.events().update(calendar_id=calendar_id, eventId=event_id, body=event_body, sendNotifications=notify).execute()






