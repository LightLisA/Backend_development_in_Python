from sqlalchemy import select
from database import new_session, TasksOrmTable
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrmTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TasksOrmTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.from_orm(task_model) for task_model in task_models]
            return tasks_schemas
