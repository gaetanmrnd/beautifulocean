from django.db import models

class Obstacle(models.Model):
	obstacle_type = models.PositiveSmallIntegerField()					#	0 = Wreck	1 = Obstruction	2 = Rock
	lat = models.DecimalField(max_digits=10, decimal_places=7)
	lon = models.DecimalField(max_digits=10, decimal_places=7)