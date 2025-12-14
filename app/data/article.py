import string

import nanoid
from tortoise import fields, models

from app.constant import Platform
from app.data.mixin import GuidMixin, TimestampMixin


class Article(GuidMixin, TimestampMixin):
    title = fields.CharField(255)
    author = fields.CharField(128)
    summary = fields.TextField()
    content = fields.TextField(null=True)
    published_at = fields.DatetimeField(null=True)

    platforms: fields.ReverseRelation['ArticlePlatform']
    tags: fields.ReverseRelation['ArticleTag']

    @classmethod
    def generate_aid(cls) -> str:
        alphabet = string.digits + string.ascii_letters
        return nanoid.generate(alphabet=alphabet, size=21)


class ArticlePlatform(GuidMixin, TimestampMixin):
    article = fields.ForeignKeyField('models.Article', related_name='platforms')
    name = fields.CharEnumField(Platform)
    url = fields.CharField(255, null=True)

    is_content_showable = fields.BooleanField(default=False, description='Whether the article detail is showable')

    class Meta:
        unique_together = (('article', 'platform'),)


class Tag(GuidMixin):
    name = fields.CharField(50, unique=True)
    articles: fields.ReverseRelation['ArticleTag']

    def __str__(self) -> str:
        return self.name


class ArticleTag(models.Model):
    id = fields.IntField(primary_key=True)
    article = fields.ForeignKeyField('models.Article', related_name='tags')
    tag = fields.ForeignKeyField('models.Tag', related_name='articles')

    class Meta:
        unique_together = (('article', 'tag'),)
