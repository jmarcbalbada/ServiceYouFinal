from django.db import models


#  Create your models here.
# [Marc] - implemented 7 tables Client, Worker, Service, ServiceRequest, Payment, RateService, PostService
# Will be calling Customer -> Client

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return str(self.clientID)


class Worker(models.Model):
    workerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return str(self.workerID)


class Service(models.Model):
    serviceID = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return str(self.serviceID)


class ServiceRequest(models.Model):
    requestID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    workerID = models.ForeignKey(Worker, on_delete=models.CASCADE)
    serviceID = models.ForeignKey(Service, on_delete=models.CASCADE)
    requestDate = models.DateField()
    status = models.IntegerField()
    dateAccepted = models.DateField()
    dateFinished = models.DateField()

    def __str__(self):
        return str(self.requestID)


class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    requestID = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    workerID = models.ForeignKey(Worker, on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentDate = models.DateField()
    amountDate = models.FloatField()
    amountPaid = models.FloatField()

    def __str__(self):
        return str(self.paymentID)


class RateService(models.Model):
    rateID = models.AutoField(primary_key=True)
    requestID = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    rateValue = models.IntegerField()
    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.rateID)


class PostService(models.Model):
    postID = models.AutoField(primary_key=True)
    workerID = models.ForeignKey(Worker, on_delete=models.CASCADE)
    serviceID = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postID)