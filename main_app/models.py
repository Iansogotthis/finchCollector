from django.utils import timezone
from datetime import timedelta
from django.db import models

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    habitat = models.CharField(max_length=50, default='forest')  # Default value set to 'forest'
    age = models.IntegerField()
    last_fed_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    def get_feeding_status(self):
        if self.last_fed_date is not None and self.last_fed_date > timezone.now() - timedelta(days=1):
            return 'Fed'
        else:
            return 'Hungry'

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    
    meal = models.CharField(max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0])

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    