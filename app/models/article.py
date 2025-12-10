from pydantic import BaseModel, Field


class PlatfromData(BaseModel):
    id: str
    name: str
    url: str
    is_content_showable: bool


class TagData(BaseModel):
    id: str
    name: str


class GetArticleData(BaseModel):
    aid: str
    title: str
    summary: str
    content: str | None = Field(None)

    platforms: list[PlatfromData]
    tags: list[TagData]


class FindArticleParams(BaseModel):
    page: int = Field()
    size: int = Field()


class FindArticleData(BaseModel):
    page: int = Field()
    size: int = Field()
    total: int = Field()
    articles: list[GetArticleData]
