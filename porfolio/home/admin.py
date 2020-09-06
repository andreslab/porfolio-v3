from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Project) 
admin.site.register(Blog) 
admin.site.register(Contact)
admin.site.register(Message)