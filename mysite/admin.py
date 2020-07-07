from django.contrib import admin
from mysite.models import Food
@admin.register(Food)
class ViewAdmin(admin.ModelAdmin):
  pass

