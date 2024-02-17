from django.contrib import admin
from .models import Complaint, CustomUser

# Register your models here.
admin.site.register(Complaint)
admin.site.register(CustomUser)
