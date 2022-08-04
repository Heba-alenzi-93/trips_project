from django.contrib import admin
from .models import Trip, Profile

# Register your models here.
class TripAdmin(admin.ModelAdmin):
    list_display =  ("id","title","description")
    list_filter = ("title",)
# Register your models here.
admin.site.register(Trip,TripAdmin)
admin.site.register(Profile)