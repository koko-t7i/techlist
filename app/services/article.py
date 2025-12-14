from app.data.article import Article
from app.model.article import GetArticleData, PlatfromData, TagData
from app.services.base import Manager
from logx import log


class ArticleManage(Manager):
    def __init__(self) -> None:
        super().__init__()

    async def get_article(self, aid: str) -> GetArticleData:
        log.info(f'get article: {aid}')
        if not (article := await Article.get_or_none(aid=aid).prefetch_related('platforms', 'tags__tag')):
            raise ValueError(f'Article[{aid}] not found')

        platforms = [
            PlatfromData(
                id=platform.id,
                name=platform.name.value,
                url=platform.url,
                is_content_showable=platform.is_content_showable,
            )
            for platform in article.platforms
        ]
        tags = [TagData(id=t.tag.id, name=t.tag.name) for t in article.tags]

        return GetArticleData(
            aid=article.id,
            title=article.title,
            summary=article.summary,
            content=article.content,
            platforms=platforms,
            tags=tags,
        )
