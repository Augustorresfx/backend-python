from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField(max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
         return self.title + "- by " + self.user.username