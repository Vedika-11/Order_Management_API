from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    status_choices=[
        ('placed','Placed'),
        ('processed','Processed'),
        ('delivered','Delivered'),
        ('canceled','Canceled')
    ]

    order_id=models.AutoField(primary_key=True)
    customer_id=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=10,choices=status_choices,default='placed')
    order_date=models.DateField()

    def calculate_total(self):
        return self.quantity * self.price
    def __str__(self):
        return f"order {self.order_id}"
    
class OrderHistory(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    action=models.CharField(max_length=50)
    timestamp=models.DateTimeField(auto_now_add=True)

