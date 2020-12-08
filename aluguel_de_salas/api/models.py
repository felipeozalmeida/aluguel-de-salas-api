from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    birthday = models.DateField()
    phone = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  editable=False)
    updated_at = models.DateTimeField(auto_now=True,  editable=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Customer'

class Room(models.Model):
    name = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    description = models.TextField()
    price = models.FloatField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  editable=False)
    updated_at = models.DateTimeField(auto_now=True,  editable=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Room'

class Rent(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    room = models.ForeignKey(Room, models.CASCADE)
    value = models.FloatField()
    start = models.DateField()
    end = models.DateField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  editable=False)
    updated_at = models.DateTimeField(auto_now=True,  editable=False)

    class Meta:
        verbose_name = 'Rent'
