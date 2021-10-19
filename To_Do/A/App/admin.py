from django.contrib import admin
from .models import ToDo



@admin.register(ToDo)
class ToDo(admin.ModelAdmin):
    list_display = ['title','complete','created_at']
    list_filter = ['complete','created_at']
    redonly_fileds =  ['created_at']
    

