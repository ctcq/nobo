from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped
from sqlalchemy import Column, ForeignKey, String, Integer, Table


class Base(DeclarativeBase):
    pass


association_table = Table(
    "notes_tags",
    Base.metadata,
    Column("note_id", ForeignKey("note.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class Tag(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: str = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Tag(name={self.name})"


class Note(Base):
    __tablename__ = "note"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: str = Column(String)
    priority: int = Column(Integer)

    tags: Mapped[list[Tag]] = relationship("Tag", secondary=association_table, backref="notes")

    def __repr__(self) -> str:
        return f"Note(id={self.id}, text={self.text}, priority={self.priority}, tags={self.tags})"


from sqlalchemy import create_engine

engine = create_engine("sqlite:///db.sqlite", echo=False, future=True)
Base.metadata.create_all(engine)
