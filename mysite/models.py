from django.db import models
# Create your models here.

class Food(models.Model): #name of table
    Name = models.CharField(max_length=100, blank = False) #item name?

    choices = (
        ('Stable', 'There is no excess or shortage of this food'),
        ('Excess', 'There is an excess of this food'),
        ('Shortage', 'There is a shortage of this food')
    )

    Status = models.CharField(max_length=100, choices=choices, blank = False) #stable/excess/shortage?
    Amount = models.IntegerField(blank = True) #optional exact amount

    def __str__(self):
        return 'Name : {0} Status : {1}' .format(self.Name, self.Status)
