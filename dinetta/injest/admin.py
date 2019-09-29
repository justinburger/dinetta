from django.contrib import admin

# Register your models here.

from .models import Camera
from .models import CameraGroup


admin.site.register(Camera)
admin.site.register(CameraGroup)
