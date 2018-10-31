import persistent

class Coworking(persistent.Persistent):
  def __init__(self, app):
    self.app= app
