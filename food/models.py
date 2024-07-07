from django.db import models
from useraccount.models import User
from auditlog.registry import auditlog


    
class SystemSetting(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    slogan = models.CharField(max_length=300)
    about = models.TextField(blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15) 
    logo = models.ImageField(upload_to='sys')
    location = models.URLField(blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    foodname = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    restimg = models.ImageField(upload_to='resto',blank=True,null=True)
    map = models.URLField(null=True,blank=True)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    # Adding image fields
    image1 = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DeliveryAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='DeliveryAddresss')
    address = models.TextField(null=True,blank=True)
    phone = models.CharField(max_length=15, null=True,blank=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.address


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return self.customer.first_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.menu_item.name

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Cash on Delivery', 'Cash on Delivery')])
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user.first_name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - Seats: {self.seats} in {self.restaurant.name}"


class BookTable(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField(blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return f"{self.customer.first_name} - Table {self.table.table_number} in {self.table.restaurant.name} on {self.reservation_time} at {self.reservation_time}"
    


class ContactUs(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contactuss')
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.customer.first_name






auditlog.register(Restaurant)
auditlog.register(MenuItem)
auditlog.register(SystemSetting)
auditlog.register(Order)
auditlog.register(OrderItem)
