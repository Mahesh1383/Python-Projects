from django.contrib import admin
from .models import NewTask

# Register your models here.
class NewTaskAdmin(admin.ModelAdmin):
    list_display = ("AddTask","time")
admin.site.register(NewTask,NewTaskAdmin)