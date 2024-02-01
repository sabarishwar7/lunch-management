from django.contrib import admin

from order.models import *

# Register your models here.

admin.site.register(detail)
admin.site.register(menu)
admin.site.register(Order)
admin.site.register(Dish)