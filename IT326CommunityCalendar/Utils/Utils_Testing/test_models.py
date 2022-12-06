from IT326CommunityCalendar.event_finder.models import Users, Event, Comment, RSVP


first_event = Event.objects.get(event_id=1)
print(first_event)