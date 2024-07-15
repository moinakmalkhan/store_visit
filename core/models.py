from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='stores')

    def __str__(self):
        return self.name

class Visit(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='visits')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='visits')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.store.name} visit by {self.employee.name} at {self.date_time}'
