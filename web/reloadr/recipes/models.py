from django.db import models

class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return self.name

class Wad(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.manufacturer) + ' ' + self.name

class Gauge(models.Model):
	size = models.CharField(max_length=20)
	def __unicode__(self):
		return str(self.size)

class HullLength(models.Model):
	length = models.CharField(max_length=20)
	def __unicode__(self):
		return self.length + ' Inch'

class Hull(models.Model):
	length = models.ForeignKey(HullLength)
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.length) + ' ' + self.name

class Powder(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.manufacturer) + ' ' + self.name

class Shot(models.Model):
	weight = models.CharField(max_length=200)
	def __unicode__(self):
		return self.weight

class Recipe(models.Model):
	powder = models.ForeignKey(Powder)
	powderWeight = models.FloatField()
	estPressure = models.IntegerField()
	estVelocity = models.IntegerField()
	shot = models.ForeignKey(Shot)
	hull = models.ForeignKey(Hull)
	hullLength = models.ForeignKey(HullLength)
	gauge = models.ForeignKey(Gauge)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return str(self.powderWeight)+str(self.powder)+str(self.gauge)+str(self.hullLength)+str(self.hull)
