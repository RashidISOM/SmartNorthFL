from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.


class Pantry(models.Model):

    name = models.CharField(max_length = 100)
    zipCode = models.CharField(max_length = 50)
    streetAdd1 = models.CharField(max_length = 100)
    streetAdd2 = models.CharField(max_length = 100, blank=True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 2)
    distance = models.IntegerField(blank=True)


    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    description = models.CharField(max_length = 1000, blank=True)

    websiteURL = models.CharField(max_length = 1000, blank=True)
    
    account = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    
    monday_start = models.TimeField(blank=True)
    monday_end = models.TimeField(blank=True)

    tuesday_start = models.TimeField(blank=True)
    tuesday_end = models.TimeField(blank=True)

    wednesday_start = models.TimeField(blank=True)
    wednesday_end = models.TimeField(blank=True)

    thursday_start = models.TimeField(blank=True)
    thursday_end = models.TimeField(blank=True)

    friday_start = models.TimeField(blank=True)
    friday_end = models.TimeField(blank=True)

    saturday_start = models.TimeField(blank=True)
    saturday_end = models.TimeField(blank=True)

    sunday_start = models.TimeField(blank=True)
    sunday_end = models.TimeField(blank=True)

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
        return '{0}' .format(self.name)


    def getZipCode(self):
        return self.zipCode

class Food(models.Model): #name of table
    Name = models.CharField(max_length=100, blank = False) #item name?

    choices = (
        ('Stable', 'There is no excess or shortage of this food'),
        ('Excess', 'There is an excess of this food'),
        ('Shortage', 'There is a shortage of this food')
    )

    Status = models.CharField(max_length=100, choices=choices, blank = False) #stable/excess/shortage?
    Amount = models.IntegerField(blank = True) #optional exact amount

    Pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)

    def __str__(self):
        return 'Name : {0} Status : {1}' .format(self.Name, self.Status)


class Mail(models.Model):
    Subject = models.CharField(max_length=100, blank=False)
    Message = models.CharField(max_length=500, blank=False)
    def __str__(self):
        return 'Subject : {0} Message : {1}' .format(self.Subject, self.Message)
    
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
    dayNames = [
        ("Monday"),
        ("Tuesday"),
        ("Wednesday"),
        ("Thursday"),
        ("Friday"),
        ("Saturday"),
        ("Sunday")
    ]
    #https://stackoverflow.com/questions/12216771/django-objects-for-business-hours
    weekday = models.IntegerField(
        choices=DAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)
    def __str__(self):
        return '{0}: From {1} - {2}' .format(self.dayNames[self.weekday], self.from_hour, self.to_hour)


class Need(models.Model):
    itemName = models.CharField(max_length = 100)
    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)
    def __str__(self):
        return '{0}' .format(self.itemName)

class Donor(models.Model):
    name = models.CharField(max_length = 100)

    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    email = models.EmailField()

    pantry = models.ForeignKey(Pantry, on_delete = models.CASCADE)
    def __str__(self):
        return 'Name : {0}' .format(self.name)

class Location(models.Model):
    zipCode = models.IntegerField()

    def __str__(self):
      return zipCode

