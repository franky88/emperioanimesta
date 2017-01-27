from django.db import models

# Create your models here.
class Artist(models.Model):
	first_name=models.CharField(max_length=60)
	middle_name=models.CharField(max_length=60)
	last_name=models.CharField(max_length=60)
	extension_name=models.CharField(max_length=5, blank=True)
	def full_name(self):
		fullname="%s %s. %s %s"%(self.first_name, self.middle_name[0], self.last_name, self.extension_name)
		return fullname

	def __str__(self):
		return self.full_name()