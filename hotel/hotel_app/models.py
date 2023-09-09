from django.db import models
from django.utils import timezone


class Room(models.Model):
    CATEGORY_CHOICES = [
        ('cheap', 'Дешёвые'),
        ('comfortable', 'Комфортные'),
        ('vip', 'V.I.P.'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    number = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    is_booked = models.BooleanField(default=False)
    features = models.ManyToManyField('RoomFeature', blank=True)
    cost_per_day = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.number


class RoomFeature(models.Model):
    name = models.CharField(max_length=100)
    cost_per_day = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class BookingApplication(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    additional_services = models.ManyToManyField(RoomFeature, blank=True)
    is_approved = models.BooleanField(default=False)
    final_price = models.PositiveIntegerField(null=True, blank=True)


    def calculate_total_nights(self):
        stay_duration = (self.check_out_date - self.check_in_date).days
        return stay_duration

    def calculate_base_price(self):
        total_nights = self.calculate_total_nights()
        return total_nights * self.room.cost_per_day

    def calculate_additional_services_cost(self):
        return sum(feature.cost_per_day for feature in self.additional_services.all())

    def calculate_final_price(self):
        base_price = self.calculate_base_price()
        additional_services_cost = self.calculate_additional_services_cost()
        return base_price + additional_services_cost

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)



        self.final_price = self.calculate_final_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заявка от {self.name} {self.surname} на {self.room.number}"
