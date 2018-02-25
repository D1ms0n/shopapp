from django.contrib import admin
from .models import *

from django.contrib.sessions.models import Session


# Register your models here.
admin.site.register(InstaUser)
admin.site.register(InstaMedia)
admin.site.register(InstaMediaSRC)
admin.site.register(InstaShopItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Session)
admin.site.register(InstaUserCred)

