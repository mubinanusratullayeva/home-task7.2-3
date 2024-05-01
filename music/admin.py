from django.contrib import admin

from .models import Artist, Album, Song


# Register your models here.
admin.site.register([Artist, Album, Song])
