from django.contrib import admin
from openstack.models import instance, flavor, images
# Register your models here.

admin.site.register(instance)
admin.site.register(flavor)
admin.site.register(images)