from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    username = models.CharField(validators=[MinLengthValidator(2)], max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.URLField(blank=True)


class Plant(models.Model):
    INDOOR_PLANTS = 'Indoor Plants'
    OUTDOOR_PLANTS = 'Outdoor Plants'

    CHOICES = (
        (INDOOR_PLANTS, 'Indoor Plants'),
        (OUTDOOR_PLANTS, 'Outdoor Plants'),
    )

    plant_type = models.CharField(max_length=14, choices=CHOICES)
    name = models.CharField(validators=[MinLengthValidator(2)], max_length=20)
    image_url = models.URLField(blank=True)
    description = models.TextField()
    price = models.FloatField()