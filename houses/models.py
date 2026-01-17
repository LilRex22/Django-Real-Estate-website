from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class House(models.Model):
    Title = models.CharField(max_length=200)
    Location = models.CharField(max_length=100)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    bed_room = models.IntegerField()
    bath = models.IntegerField()
    square_ft = models.IntegerField()
    image = models.ImageField(null=True)
    sitting_room = models.ImageField(null=True)
    kitchen = models.ImageField(null=True)
    bathroom = models.ImageField(null=True)
    bedroom = models.ImageField(null=True)
    sale = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Title
    
    
class Newsletter_Email(models.Model):
    email = models.EmailField(max_length=200)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email