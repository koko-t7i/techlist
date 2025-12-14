from fastapi import Request, Response, status

from app.api import BaseRouter, DashRouter
from app.api.deps import ExampleMgt
from app.model.example import CreateExampleParams, ExampleBase

router = BaseRouter(route_class=DashRouter)


@router.get('/{example_id}', response_model=ExampleBase)
async def get_example(request: Request, response: Response, example_mgt: ExampleMgt, example_id: int) -> ExampleBase | None:
    example = await example_mgt.get_example(example_id)
    return example


@router.post('', response_model=ExampleBase, status_code=status.HTTP_201_CREATED)
async def create_example(
    request: Request, response: Response, example_mgt: ExampleMgt, params: CreateExampleParams
) -> ExampleBase:
    example = await example_mgt.create(params)
    return example
