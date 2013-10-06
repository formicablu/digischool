from django.contrib.gis.db import models

class Year(models.Model):
	name = models.IntegerField()
	def __str__(self):
		return self.name

class School(models.Model):
	name = models.CharField(max_length=255)
	position = models.PointField()

	def __str__(self):
		return self.name

class MetricType(models.Model):
	name = models.CharField(max_length=500)
	mtype = models.CharField(max_length=5, choices=[('str', 'String'), ('int', 'Integer'), ('float', 'Float'), ('bool', 'Boolean')])
	def __str__(self):
		return self.name

class Metric(models.Model):
	school = models.ForeignKey(School)
	year = models.ForeignKey(Year)
	metric_value = models.TextField()
	metric_type = models.ForeignKey(MetricType)

	def __str__(self):
		return "%s - %s:%s = %s" % (self.school, self.year, self.metric_type, self.metric_value)
		

