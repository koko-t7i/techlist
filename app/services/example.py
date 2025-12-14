from app.data import Example
from app.model.example import CreateExampleParams, ExampleBase


class ExampleManage:
    @classmethod
    async def get_example(cls, example_id: int) -> ExampleBase | None:
        if example := await Example.get_or_none(id=example_id):
            return ExampleBase(**example.model_dump())
        return None

    @classmethod
    async def create(cls, params: CreateExampleParams) -> ExampleBase:
        example = await Example.create(**params.model_dump())
        return ExampleBase(**example.model_dump())
