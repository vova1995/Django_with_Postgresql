from django.db import models

# Create your models here.


class Check(models.Model):
	name = models.CharField(max_length=150, default='')
	age = models.IntegerField(default=0)

	def __str__(self):
		return self.name + 'the age: ' + str(self.age)