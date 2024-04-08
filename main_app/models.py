from django.db import models

class Finch(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    habitat = models.CharField(max_length=50, default='forest')  # Default value set to 'forest'
    age = models.IntegerField()

    def __str__(self):
        return self.name