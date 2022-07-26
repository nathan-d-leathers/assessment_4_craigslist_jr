from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.CharField(max_length=255, unique=True, blank=False)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=500, blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# Update: Need to add blank = False to each CharField
