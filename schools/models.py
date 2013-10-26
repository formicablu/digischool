
from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Year(models.Model):
	name = models.IntegerField()
	def __str__(self):
		return str(self.name)

class School(models.Model):
	name = models.CharField(max_length=255)
	position = models.PointField()
	objects = models.GeoManager()
	
	def all_metrics(self, year=None):
		ret = {}
		for metric in self.metrics.all():
			if not metric.year.name in ret:
				ret[metric.year.name] = {}
			if metric.metric_type.id in ret[metric.year.name]:
				ret[metric.year.name][metric.metric_type.id].append(metric.value())
			else:
				ret[metric.year.name][metric.metric_type.id] = [metric.value()]
		return ret

	def __str__(self):
		return self.name

class MetricType(models.Model):
	name = models.CharField(max_length=500)
	mtype = models.CharField(max_length=5, choices=[('str', 'String'), ('int', 'Integer'), ('float', 'Float'), ('bool', 'Boolean')])
	values = models.TextField(blank=True, null=True)
	unit = models.CharField(max_length=10, blank=True, null=True)
	icon = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.name

class Metric(models.Model):
	school = models.ForeignKey(School,related_name="metrics")
	year = models.ForeignKey(Year)
	metric_value = models.TextField()
	metric_type = models.ForeignKey(MetricType)

	def value(self):
		op = {
			"str":str,
			"int":int,
			'float':float,
			'bool':bool
		}
		return op[self.metric_type.mtype](self.metric_value)

	def __str__(self):
		return "%s - %s:%s = %s %s" % (self.school, self.year, self.metric_type, self.metric_value, self.metric_type.unit)
		

class MetricEvaluation(models.Model):
	metric = models.ForeignKey(Metric)
	is_true = models.BooleanField(default=True)
	user = models.ForeignKey(User)