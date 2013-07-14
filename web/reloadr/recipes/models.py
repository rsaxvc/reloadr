from django.db import models

class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return self.name

class Gauge(models.Model):
	size = models.CharField(max_length=20)
	def __unicode__(self):
		return str(self.size) + ' Gauge'

class PrimerSize(models.Model):
	size = models.CharField(max_length=20)
	def __unicode__(self):
		return str(self.size) + '"'	

class Primer(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	size = models.ForeignKey(PrimerSize)
	name = models.CharField(max_length=20)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.manufacturer) + ' ' + unicode(self.name)

class Wad(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	gauge = models.ForeignKey(Gauge)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.manufacturer) + ' ' + self.name

class HullLength(models.Model):
	length = models.CharField(max_length=20)
	def __unicode__(self):
		return self.length + ' Inch'

class Hull(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	length = models.ForeignKey(HullLength)
	gauge = models.ForeignKey(Gauge)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode( self.manufacturer ) + ' ' + unicode(self.gauge) + ' ' + unicode(self.length) + ' ' + self.name

class Powder(models.Model):
	manufacturer = models.ForeignKey(Manufacturer)
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return unicode(self.manufacturer) + ' ' + self.name

class ShotWeight(models.Model):
	weight = models.CharField(max_length=200)
	def __unicode__(self):
		return self.weight + ' oz';

class ShotType(models.Model):
	type = models.CharField(max_length=200)
	def __unicode__(self):
		return self.type	

class Recipe(models.Model):
	powder = models.ForeignKey(Powder)
	shotType = models.ForeignKey(ShotType)
	shotWeight = models.ForeignKey(ShotWeight)
	hull = models.ForeignKey(Hull)
	hullLength = models.ForeignKey(HullLength)
	gauge = models.ForeignKey(Gauge)
	primer = models.ForeignKey(Primer)

	powderWeight = models.FloatField()
	estPressure = models.IntegerField()
	estVelocity = models.IntegerField()

	url = models.CharField(max_length=2048)
	def __unicode__(self):
		return str(self.powderWeight)+str(self.powder)+str(self.gauge)+str(self.hullLength)+str(self.hull)
