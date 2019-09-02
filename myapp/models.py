from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Pet(models.Model):
	name = models.CharField(max_length=60)
	age = models.IntegerField()
	available = models.BooleanField(default=True)
	image = models.ImageField(null=True)
	price = models.DecimalField(max_digits=4, decimal_places=2)