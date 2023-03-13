from django.contrib import admin
from .models import Movie,Student,Slides

# Register your models here.
admin.site.register(Movie)
admin.site.register(Student)
admin.site.register(Slides)