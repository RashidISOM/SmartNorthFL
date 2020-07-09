from django.db import models
from django.core.validators import RegexValidator
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

    #pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)

    def __str__(self):
        return 'Name : {0} Status : {1}' .format(self.Name, self.Status)

class Pantry(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length=250)
    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    description = models.CharField(max_length = 1000)

    websiteURL = models.CharField(max_length = 1000)


    #users
    #notifiers
    #name
    #address
    #phone number
    #Description
    #hours
    #website URL
    #items in need of
    #food/inventory
    def __str__(self):
        return 'Name : {0}' .format(self.name)

class Hours(models.Model):
    DAYS = [
        (1, ("Monday")),
        (2, ("Tuesday")),
        (3, ("Wednesday")),
      (4, ("Thursday")),
      (5, ("Friday")),
      (6, ("Saturday")),
      (7, ("Sunday")),
    ]
    #https://stackoverflow.com/questions/12216771/django-objects-for-business-hours
    weekday = models.IntegerField(
        choices=DAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)


class Need(models.Model):
    itemName = models.CharField(max_length = 100)
    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)
    def __str__(self):
        return 'Name : {0}' .format(self.itemName)

class Donor(models.Model):
    name = models.CharField(max_length = 100)

    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    email = models.EmailField()

    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)
    def __str__(self):
        return 'Name : {0}' .format(self.name)
