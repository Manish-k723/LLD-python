from datetime import datetime, timedelta

from GoogleCalendarV2.enums import RSVPStatus, RecurringFrequency
from GoogleCalendarV2.facade import GoogleCalendarFacade
from GoogleCalendarV2.models import Location, RecurrenceRule


def run_demo() -> None:
    app = GoogleCalendarFacade()

    alice_id = app.register_user("Alice", "alice@example.com")
    bob_id = app.register_user("Bob", "bob@example.com")

    calendar_id = app.create_calendar(alice_id, "Alice Work")

    start = datetime(2026, 6, 1, 10, 0)
    end = start + timedelta(hours=1)

    event = app.schedule_event(
        calendar_id=calendar_id,
        created_by=alice_id,
        title="Sprint Planning",
        start_time=start,
        end_time=end,
        attendee_ids=[bob_id],
        description="Plan sprint deliverables",
        location=Location("Meeting Room A", 6),
        recurrence=RecurrenceRule(frequency=RecurringFrequency.WEEKLY, interval=1, count=3),
    )

    app.respond_to_invite(event.id, bob_id, RSVPStatus.ACCEPTED)

    print("\nEvent list:")
    for e in app.list_events(calendar_id):
        print(f"- #{e.id} {e.title} [{e.start_time} - {e.end_time}] status={e.status.value}")

    print("\nOccurrences:")
    for s, t in app.event_occurrences(event.id):
        print(f"- {s} -> {t}")

    try:
        app.schedule_event(
            calendar_id=calendar_id,
            created_by=bob_id,
            title="Conflicting Event",
            start_time=start + timedelta(minutes=30),
            end_time=end + timedelta(minutes=30),
            attendee_ids=[alice_id],
        )
    except ValueError as exc:
        print(f"\nConflict check works: {exc}")


if __name__ == "__main__":
    run_demo()
