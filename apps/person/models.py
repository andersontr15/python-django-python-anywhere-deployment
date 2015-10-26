from django.db import models

class Person(models.Model):
	first_name = models.TextField(blank=False, max_length=20)
	last_name = models.TextField(blank=False, max_length=20)
	zip_code = models.IntegerField(blank=False)
	city = models.TextField(blank=False, max_length=20)

