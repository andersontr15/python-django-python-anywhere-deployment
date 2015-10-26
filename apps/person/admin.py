from django.db import models
from apps.person.models import Person
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'city', 'zip_code')
	search_fields = ['first_name', 'last_name', 'city', 'zip_code']
	
admin.site.register(Person, PersonAdmin)
