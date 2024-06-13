from django.db import models

class Event(models.Model):
    name_event = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name_event


class Attendance(models.Model):
    event = models.ManyToManyField('Event')
    participant = models.ManyToManyField('participantes.Participant')

    def __str__(self):
        return f"Asistencia de {self.pk} a {self.event.name_event}"
