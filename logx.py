from dataclasses import dataclass
from typing import Literal
from loguru import logger

@dataclass
class LogConfig:
    development: bool
    encoding: Literal['json', 'console']
    time_key: str = 'time'



log = logger