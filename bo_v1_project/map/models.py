from django.db import models

class Wreck(models.Model):
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	long = models.DecimalField(max_digits=9, decimal_places=6)