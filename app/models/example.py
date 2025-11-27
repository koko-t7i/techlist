from tortoise import models, fields


class Example(models.Model):
    """Example model for demonstration"""

    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255, description='Example name')
    description = fields.CharField(max_length=500, description='Example description')

    class Meta:
        table = 'examples'

    def model_dump(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }
