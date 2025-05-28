from django.contrib import admin
from .models import *
from atexit import register

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)