from __future__ import unicode_literals

from django.db import models


class User_info(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    sex = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='avatars', height_field=50, width_field=50)
