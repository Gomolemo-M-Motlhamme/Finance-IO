from django.db import models

# Create your models here.
class Income(models.Model):
    income = models.CharField(max_length=500)
    amount = models.FloatField()

    def __str__(self):
        return (f"{self.income} {self.amount}")
    
class Expense(models.Model):
    expense = models.CharField(max_length=500)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return (f"{self.expense} {self.amount} {self.date}")