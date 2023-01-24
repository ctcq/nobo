from model import engine, Note
from sqlalchemy.orm import Session
from random import sample


def delete(id: int):
    with Session(engine) as session:
        note = session.get(Note, id)

        if note is None:
            print(f"Note with given id does not exist")
        else:
            if input(f"Delete note {note}? (y/N) ") == "y":
                session.delete(note)
                session.commit()
                print("Note deleted!")
