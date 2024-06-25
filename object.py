from uuid import uuid4, UUID
from enum import Enum

objects = {}

class Object:
  uuid = None
  callbacks = None
  
  def __init__(self) -> None:
    self.uuid = uuid4()
    objects[self.uuid] = self

  def delete(self) -> None:
    objects.pop(self.uuid, None)
