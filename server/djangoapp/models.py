from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake,on_delete=models.CASCADE
    )  # Many-to-One relationship
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    MOTOR_TYPES = [
        ('INLINE', 'Inline'),
        ('V-TYPE', 'V-Type'),
    ]
    motor_type = models.CharField(
        max_length=10, choices=MOTOR_TYPES, default='INLINE'
    )

    def __str__(self):
        return self.name
