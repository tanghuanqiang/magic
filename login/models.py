from django.db import models
class Person(models.Model):
	id = models.IntegerField('id',primary_key=True)
	name = models.CharField(max_length=30)
	photo =models.ImageField(max_length=100)
	sex =  models.CharField(max_length=10)

	def __str__(self):
		return self.name
