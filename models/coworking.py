import persistent, transaction
from aplicacion import aplicacion

class Coworking(persistent.Persistent):
  def __init__(self, app):
    self.app= app
