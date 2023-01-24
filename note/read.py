from model import engine, Note
from sqlalchemy import select
from sqlalchemy.orm import Session
from random import sample


def read(amount: int, min_priority: int, max_priority: int, random: bool):
    with Session(engine) as session:
        stmt = select(Note).order_by(Note.priority)
        conditions = (Note.priority >= min_priority, Note.priority <= max_priority)
        notes = session.scalars(stmt.where(*conditions)).all()

        if random:
            print(sample(notes, k=amount))
        else:
            print(notes[:amount])
