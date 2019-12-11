from django.contrib import admin

# Register your models here.
from .models import Laptop , Student
admin.site.register(Laptop)
admin.site.register(Student)
