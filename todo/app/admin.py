from django.contrib import admin
from .models import Todopage
# Register your models here.


class todoModel(admin.ModelAdmin):
    list_display = ['tasks']


admin.site.register(Todopage, todoModel)
