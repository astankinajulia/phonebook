from django.contrib import admin

from api.models import Company, Employee, PhoneNumber

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(PhoneNumber)
