from django.contrib import admin
from .models import *
from .models import Profile

# Register your models here.
admin.site.register(Project)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Profile)