from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dish(models.Model):
    numeration = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100, verbose_name="Назва блюда")
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
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name

class Shopcart(models.Model):
    item = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item', 'user'], name='unique_item_user')
        ]

    def get_total_price(self):
        return self.item.price * self.quantity

    def __str__(self):
        return f"{self.quantity}  {self.item.name} для {self.user.username}"
    






"""class LastStep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carts = models.ManyToManyField(Shopcart)
    total_price = models.PositiveIntegerField(default=0)

    def update_total_price(self):
        for i in self.carts:
            self.total_price = self.Dish.price * self.Shopcart.quantity
            total_price = models.Sum(total_price, )

    

    def __str__(self):
        return f"Заказ для {self.user.username} - Загальна сума: {self.total_price}" """

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення {self.id} для {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.dish.price * self.quantity