from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):                    # model - class    - table
    bookid = models.IntegerField()  # field - instance - row
    title = models.CharField(max_length=255)  # field - instance - row
    author = models.CharField(max_length=255)  # field - instance - row
    description = models.CharField(max_length=255)  # field - instance - row

