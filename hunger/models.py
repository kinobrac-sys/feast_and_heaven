from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Position(models.Model):
    numeration = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    category1 = [
        ("Перше блюдо", "Перше блюдо"),
        ("Друге блюдо", "Друге блюдо"),
        ("Десерт", "Десерт"),
        ("Напій", "Напій"),
        ("Закуска", "Закуска"),
        ("Салат", "Салат"),
        ("Гостра", "Гостра"),
    ]
    category = models.CharField(max_length=100, choices=category1)
    price = models.PositiveIntegerField(default=150)






class Reservation(models.Model):
    stravu = models.ForeignKey(Position, on_delete=models.CASCADE)
    reservator = models.ForeignKey(User, on_delete=models.CASCADE)
    tables = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
    ]
    tables = models.CharField(max_length=100, choices=tables, default="1")
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_n_time = models.DateTimeField()
    time_of_reservation = models.DateTimeField(auto_now_add=True)
    people = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    ]
    number_of_people = models.PositiveIntegerField(choices=people, default="1")

    def __str__(self):
        return f"Reservation for {self.name} on {self.date_n_time}"