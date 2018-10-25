class Meeting:
  def __init__(self, details, organizer, organizer_rol, attendees, status, date, begin_hour, finish_hour):
    self.details= details
    self.organizer= organizer
    self.organizer_rol= organizer_rol
    self.attendees= attendees
    self.status= status
    self.date= date
    self.begin_hour= begin_hour
    self.finish_hour= finish_hour

  #Agendar reunion
  def schedule_meeting(self):
    pass
  #Cancelar reunion
  def cancel_meeting(self):
    pass
  #Reagendar reunion
  def reschedule_meeting(self):
    pass

#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class InformalMeeting(Meeting):
  def __init__(self, duration):
      self.duration= duration
  def begin_informal_meeting(self, begin_hour):
      pass
  def finish_informal_meeting(self, duration):
      pass

#Reunion formal: toda reunion previamente agendada
class FormalMeeting(Meeting):
  def __init__(self, registered_at):
    self.registered_at= registered_at

#Reunion formal unica: toda reunion previamente agendada que no se repite en el tiempo.
#Dura mas de 30 minutos y solo tiene fecha de inicio
class FormalUniqueMeeting(Meeting):
  def __init__(self):
      pass

#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class FormalPeriodicMeeting(FormalMeeting):
  def __init__(self, begin_date, finish_date, frequence):
      self.begin_date= begin_date
      self.finish_date= finish_date
      self.frequence= frequence
  def edit_frequence(self, frequence):
      pass
  def change_finish_date(self, finish_date):
      pass
  