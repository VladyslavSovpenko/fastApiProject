from typing import List

from fastapi import APIRouter, HTTPException

from models.models import Event

event_router = APIRouter(tags=['Events'])

events = []


@event_router.get('/', response_model=List[Event])
def get_all_events() -> List[Event]:
    return events


@event_router.get('/{event_id}', response_model=Event)
def get_event(event_id: int) -> Event:
    event = next(filter(lambda test_event: test_event.id == event_id, events))
    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    return event


@event_router.post('/new')
def create_event(event: Event) -> dict:
    events.append(event)
    return {"message": "Event created"}


@event_router.delete('/{id}', response_model=Event)
def delete_event(event_id: int) -> dict:
    event = filter(lambda event: event.id == event_id, events)
    if event:
        events.remove(event)
        return {"message": "Event deleted"}
    raise HTTPException(status_code=404, detail='Event not found')


@event_router.delete('/')
def delete_all_events() -> dict:
    events.clear()
    return {"message": "Events deleted"}
