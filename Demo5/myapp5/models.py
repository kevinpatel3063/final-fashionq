from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    phone_number = models.IntegerField(blank=True, null=True)
    adress = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name
    
class login(models.Model):
    email = models.EmailField(unique=True, max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Categories(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/images')
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Filter_Price(models.Model):
    
    FILTER_PRICE = (
        ('0 TO 500', '0 TO 500'),
        ('500 TO 1000', '500 TO 1000'),
        ('1000 TO 1500', '1000 TO 1500'),
        ('1500 TO 2000', '1500 TO 2000'),
        ('2000 TO 2500', '2000 TO 2500'),
        ('2500 TO 3000', '2500 TO 3000'),
        ('3000 TO 3500', '3000 TO 3500'),
        ('3500 TO 4000', '3500 TO 4000'),
    )
    price = models.CharField(choices=FILTER_PRICE,max_length=60)
    
    def __str__(self):
        return self.price
    
class Sub_category(models.Model):
    SUB_CATEGORY = (
                    ('Men','Men'),
                    ('Women','Women'),
                    ('Kids','Kids'),
                    ('Beauty','Beauty'),
                    )
    sub_category = models.CharField(choices=SUB_CATEGORY,max_length=200)
    def __str__(self):
        return self.sub_category
    
    
class Product(models.Model):
    CONDITION = (('New','New'),('Old','Old'))
    STOCK = (('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS = (('Publish','Publish'),('Draft','Draft'))
    
    unique_id = models.CharField(unique=True, max_length=200, null = True,blank=True)
    image = models.ImageField(upload_to='img/images')
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    condition= models.CharField(choices=CONDITION,max_length=100)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

    
class Images(models.Model):
    image = models.ImageField(upload_to='img/images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    
    
class Tag(models.Model):
    name  = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    review = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order =  models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/order")
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    total = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.order.user.username
    
    
    
    
    
    
    
    