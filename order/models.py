from django.db import models



from collections import UserList
from socket import getnameinfo

from django.contrib.auth.models import User
from datetime import datetime,timedelta





# Create your models here.
class detail(models.Model):
    username=models.CharField(max_length=40)
    e_id = models.CharField(max_length=50)
    email = models.EmailField()
    password=models.CharField(max_length=30,default=12345678)
    tkn_no=models.CharField(max_length=6, default=str("T")+str(User.id) )
   
    
    def __str__(self):
        return self.username
    def __str__(self):
        return self.email
    def get_eid(self):
        return self.e_id
    
    def __str__(self):
        return self.tkn_no



class menu(models.Model):
    
    catchoice= [
        ('food', 'Food'),
        ('snack', 'Snack'),
        ('drink', 'Drink'),
        
        ]
    cate=models.CharField(max_length=30,choices=catchoice,default='food')
    

    def __str__(self):
        return self.cate

class Dish(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(menu, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey(detail, on_delete=models.CASCADE)
    food = models.ForeignKey(Dish, on_delete=models.CASCADE)
    tkn=detail.tkn_no
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.detail.username} - {self.detail.tkn_no} - {self.Dish.name}"



'''class Menu(models.Model):
    catchoice= [
        ('food', 'Food'),
        ('snack', 'Snack'),
        ('drink', 'Drink'),
        
        ]
    name=models.CharField(max_length=30)
    
    
    cate=models.CharField(max_length=30,choices=catchoice,default='food')'''
    
    