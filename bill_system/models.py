from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField()

def __str__(self):
    return self.name     
    
class Sale(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    sales_date=models.DateTimeField(auto_now_add=True)
    
def total_price(self):
    return self.product.price*self.quantity

def __str__(self):
    return f"{self.customer.name}-{self.product.name}({self.quantity})"