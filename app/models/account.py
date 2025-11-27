import nanoid
import bcrypt
from tortoise import models, fields

from app.constant import AccountRole
from app.models.mixin import TimestampMixin


class Account(models.Model, TimestampMixin):
    uid = fields.CharField(24, primary_key=True)
    role = fields.IntEnumField(AccountRole)
    parent_id = fields.CharField(24, null=True, db_index=True)
    email = fields.CharField(128, unique=True)
    password = fields.BinaryField(description='password hash')

    @classmethod
    def generate_uid(cls, role: AccountRole) -> str:
        flag_map = {
            AccountRole.ADMIN: 'R_',
            AccountRole.USER: 'U_',
            AccountRole.GUEST: 'G_',
        }
        return flag_map[role] + nanoid.generate(alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', size=10)

    @staticmethod
    def hashpw(password: str) -> bytes:
        hash_pw = bcrypt.hashpw(password.encode('utf-8'), salt=bcrypt.gensalt())
        return hash_pw

    def checkpw(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    class Meta:
        table = 'account'
