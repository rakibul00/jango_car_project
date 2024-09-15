from django.db import models

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Dhaka','Dhaka'),
         ('Barisal','Barisal'),
          ('Cumellah','Cumellah'), 
        ('Chittagong','Chittagong'),     
        ('Khulna','Khulna'),  
        ('Rajshahi','Rajshahi'), 
        ('Ranpur','Ranpur'), 
         
    )
    id = models.IntegerField(primary_key=True)
    your_name = models.CharField(max_length=20)
   
   
    car_name = models.CharField(max_length=20)
    city = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)