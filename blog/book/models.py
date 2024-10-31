from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    birthdate=models.DateField()
    
    def __str__(self) -> str:
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=50)
    publication_date=models.DateField()
    price=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    description=models.TextField(default="")
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.title