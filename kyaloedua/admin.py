from django.contrib import admin
from .models import RoomPost, Department, Message

# Register your models here.
admin.site.register(RoomPost)
admin.site.register(Department)
admin.site.register(Message)
