from enum import IntEnum, StrEnum


class AccountRole(IntEnum):
    ADMIN = 0
    USER = 2
    GUEST = 8


class Platform(StrEnum):
    GITHUB = 'Github'
    DEV = 'Dev'
