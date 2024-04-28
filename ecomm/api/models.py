from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    isNew = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ratings = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Repair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ratings = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class SamsungRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ratings =models.FloatField(default=2)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class IphoneRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class OppoRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
class XiomiRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class RealmeRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class InfinixRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class TecnoRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url    
    
class RedmiRepair(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    oldPrice = models.FloatField()
    price = models.FloatField()
    type=models.CharField(max_length=100, null=True)
    size=models.CharField(max_length=100, null=True)
    resolution=models.CharField(max_length=100, null=True)
    protection=models.CharField(max_length=100, null=True)
    Time = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    
    image = models.ImageField(null=True, blank=True, upload_to= "images/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url