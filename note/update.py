from model import engine, Note
from sqlalchemy.orm import Session


def update(
    id: int,
    text: str = None,
    priority: str = None,
    add_tags: list[str] = [],
    remove_tags: list[str] = [],
):
    with Session(engine) as session:
        note = session.get(Note, id)
        if add_tags is not None:
            note.tags += add_tags
        if remove_tags is not None:
            note.tags = [tag for tag in note.tags if tag not in remove_tags]
        if text is not None:
            note.text = text
        if priority is not None:
            note.priority = priority

        session.add(note)
        session.commit()
