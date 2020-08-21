from django.db import models
from django.contrib.auth.models import User


    
# Create your models here.
class Chat(models.Model):
    type = models.CharField(max_length=200)
    userID1 = models.ManyToManyField(User, related_name="userID1", blank=True)
    userID2 = models.ManyToManyField(User, related_name="userID2",blank=True)
    date = models.DateField()

class UserChat(models.Model):
    user = models.ManyToManyField(User, blank=True)
    chat = models.ManyToManyField(Chat, blank=True)
    date = models.DateField()

class Message(models.Model):
    user = models.ManyToManyField(User, blank=True)
    chat = models.ManyToManyField(Chat, blank=True)
    sendDate = models.DateField()
    content = models.CharField(max_length=200)

class Employee(models.Model):
    user = models.ManyToManyField(User, blank=True)

class Role(models.Model):
    employee = models.ManyToManyField(Employee, blank=True)
    state = models.BooleanField()

class Screen(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)

class Permits(models.Model):
    role = models.ManyToManyField(Role, blank=True)
    screen = models.ManyToManyField(Screen, blank=True)
    p_modify = models.CharField(max_length=200)
    p_create = models.CharField(max_length=200)
    p_delete = models.CharField(max_length=200)
    p_read = models.CharField(max_length=200)

class Company(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200)

class Suggestion(models.Model):
    email = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    atendido = models.BooleanField()

class Vehicle(models.Model):
    brand = models.CharField(max_length=25)
    carPlate = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    

class Driver(models.Model):
    user = models.ManyToManyField(User)
    rate = models.CharField(max_length=25)
    currentVehicle = models.ManyToManyField(Vehicle)

class Client(models.Model):
    user = models.ManyToManyField(User)
    rate = models.DecimalField(decimal_places=2,max_digits=2)

class Location(models.Model):
    latitude = models.DecimalField(decimal_places=2,max_digits=2)
    longitude = models.DecimalField(decimal_places=2,max_digits=2)
    name = models.CharField(max_length=25)

class TypeService(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=25)

class Fare(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    typeService = models.ManyToManyField(TypeService, blank=True)
    minFare = models.DecimalField(decimal_places=2,max_digits=2)
    pricePerKm = models.DecimalField(decimal_places=2,max_digits=2)

class Payment(models.Model):
    fare = models.ManyToManyField(Fare)
    type = models.CharField(max_length=25)
    amount = models.DecimalField(decimal_places=2,max_digits=2)
    employeeNeed = models.CharField(max_length=25)
    chargeAmount = models.DecimalField(decimal_places=2,max_digits=2)
    total = models.DecimalField(decimal_places=2,max_digits=2)
    paymentDate = models.DateField()    

class Service(models.Model):
    client = models.ManyToManyField(Client)
    driver = models.ManyToManyField(Driver)
    startLocation = models.ManyToManyField(Location,related_name="startLocation")
    endLocation = models.ManyToManyField(Location,related_name="endLocation")
    payment = models.ManyToManyField(Payment)
    typeService = models.ManyToManyField(TypeService)
    employeeScore = models.DecimalField(decimal_places=2,max_digits=2)
    clientScore = models.DecimalField(decimal_places=2,max_digits=2)
    startTime = models.DateField()
    endTime = models.DateField()
    startDate = models.DateField()
    startDate = models.DateField()
    isReservation = models.BooleanField()
    state = models.BooleanField()

class Details(models.Model):
    service = models.ManyToManyField(Service)
    user = models.ManyToManyField(User)
    description = models.CharField(max_length=25)

