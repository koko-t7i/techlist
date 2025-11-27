import nanoid
from tortoise import models, fields

from app.constant import Platform
from app.models.mixin import TimestampMixin


class Article(models.Model, TimestampMixin):
    aid = fields.IntField(primary_key=True)
    title = fields.CharField(255)
    summary = fields.TextField()
    content = fields.TextField(null=True)

    platforms: fields.ReverseRelation['ArticlePlatform']
    tags: fields.ReverseRelation['ArticleTag']

    @classmethod
    def generate_aid(cls) -> str:
        return nanoid.generate(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', size=21)


class ArticlePlatform(models.Model, TimestampMixin):
    id = fields.IntField(primary_key=True)
    article = fields.ForeignKeyField('models.Article', related_name='platforms')
    platform = fields.CharEnumField(Platform)
    platform_url = fields.CharField(255, null=True)
    platform_id = fields.CharField(255, null=True)
    published_at = fields.DatetimeField(null=True)

    class Meta:
        unique_together = (('article', 'platform'),)


class Tag(models.Model):
    id = fields.IntField(primary_key=True)
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
