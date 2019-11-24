from django.contrib import admin
from .models import Location, Position, Organization
# Register your models here.
admin.site.register(Location)
admin.site.register(Position)
admin.site.register(Organization)
