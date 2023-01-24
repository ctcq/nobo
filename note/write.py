from model import engine, Note, Tag
from sqlalchemy import select
from sqlalchemy.orm import Session


def write(text: str, priority: int, tags: list[str]):
    with Session(engine) as session:
        note = Note(text=text, priority=priority)

        for name in tags:
            tag = session.query(Tag).filter_by(name=name).scalar()
            if tag is None:
                tag = Tag(name=name)
            note.tags.append(tag)

        session.add(note)
        session.commit()
