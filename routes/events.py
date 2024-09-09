from typing import List

from fastapi import APIRouter, HTTPException, Depends, Request, status
from sqlmodel import select

from database.connection import get_session
from models.models import Event, EventUpdate

from models.models import Event

event_router = APIRouter(tags=['Events'])

events = []


@event_router.get('/', response_model=List[Event])
async def get_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    return session.exec(statement).all()


@event_router.get('/{event_id}', response_model=Event)
async def get_event(event_id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    return event


@event_router.post('/new')
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Event created"}


@event_router.put('/{event_id}', response_model=Event)
async def update_event(event_id: int, new_event: Event, session=Depends(get_session)) -> dict:
    event = session.get(Event, event_id)
    if event:
        event_data = new_event.dict(exclude_none=True)
        for k, v in event_data.items():
            setattr(event, k, v)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(status_code=404, detail='Event not found')


@event_router.delete('/{id}', response_model=Event)
async def delete_event(event_id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, event_id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted"}
    raise HTTPException(status_code=404, detail='Event not found')


@event_router.delete('/')
async def delete_all_events(session=Depends(get_session)) -> dict:
    session.query(Event).delete()
    session.commit()
    return {"message": "Events deleted"}
