from pydantic import BaseModel, Field


class ExampleBase(BaseModel):
    id: int = Field(..., description='Example ID')
    name: str = Field(..., min_length=1, max_length=255, description='Example name')
    description: str = Field(..., min_length=1, max_length=500, description='Example description')


class CreateExampleParams(BaseModel): 
    name: str = Field(..., min_length=1, max_length=255, description='Example name')
    description: str = Field(..., min_length=1, max_length=500, description='Example description')

