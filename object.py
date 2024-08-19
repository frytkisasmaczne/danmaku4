from dataclasses import dataclass
from uuid import uuid4, UUID
from enum import Enum
import dictdiffer

objects = {}

@dataclass
class Object:
  uuid = None
  callbacks = None
  
  def __init__(self) -> None:
    self.uuid = uuid4()
    objects[self.uuid] = self

  def delete(self) -> None:
    objects.pop(self.uuid, None)
