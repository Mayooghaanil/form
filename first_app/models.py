from django.db import models


# Create your models here.

class student(models.Model):
	name=models.CharField(max_length=150)
	email=models.EmailField(max_length=150,unique=True)
	# Age=models.IntegerField()
	# address=models.TextField()
	
	def __str__(self):
		return self.name