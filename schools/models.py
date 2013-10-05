from django.db import models

class Year(models.Model):
	name = models.CharField(max_length=4)
	def __str__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=255)

class MetricType(models.Model):
	name = models.CharField(max_length=500)

class Metric
	school = models.ForeignKey(School)
	metric_value = models.IntegerField()
	metric_type = models.ForeignKey(MetricType)
		

