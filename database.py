from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"  # url or name of database + driver : /// name of file ==> our database
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class ModelBase(DeclarativeBase):
    pass


class TasksOrmTable(ModelBase):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]  # or Mapped[str | None]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
