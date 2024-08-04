from pathlib import Path
from typing import Any

from pydantic import BaseModel


class Step(BaseModel):
    name: str
    definiton: str
    params: dict[str, Any]
    inputs: list[Path]
    artifacts: list[Path]


class Experiment(BaseModel):
    name: str
    steps: list[Step]
