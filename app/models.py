from django.db import models

# Create your models here.
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    movie = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=20)
    tickets = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamp

    def __str__(self):
        return f"{self.name} - {self.movie} ({self.date} {self.time})"
