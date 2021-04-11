from django.db import models

# Create your models here.
class Employee(models.Model):
	ename=models.CharField(max_length=30)
	salary=models.FloatField()
	design=models.CharField(max_length=30)
	def __str__(self):
		return self.ename  
