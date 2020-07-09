from django.contrib import admin
from mysite.models import Food
from mysite.models import Pantry
from mysite.models import Need
from mysite.models import Donor
from mysite.models import Hours
@admin.register(Food)
@admin.register(Pantry)
@admin.register(Need)
@admin.register(Hours)
@admin.register(Donor)

class ViewAdmin(admin.ModelAdmin):
  pass
