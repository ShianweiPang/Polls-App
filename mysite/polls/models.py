from django.db import models
from datetime import datetime
from django.utils import timezone

# 3 main types of relations
# one-one, one-many/many-one, many-many
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    # Override to name each instance in the database
    def __str__(self):
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Organizer(models.Model):
    name = models.CharField(max_length=200)


# Create your models here.
# ./manage.py migrate <myapp> --fake << Google more on this
# uses python manage.py makemigrations command to create migration file for database
class Poll(models.Model):
    # take defined model to create database in sql and automatic create tables
    # CharField - standard text
    # TextField - longer text
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    organizer_email = models.EmailField()
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # intermediate table is created by Django
    # blank=True, (fields in the admin form can be empty)
    # null = True, intermediate table wont add any relation data when we create Blank for this Participant *NOT SURE
    participant = models.ManyToManyField(Participant, blank=True, null=True)

    # Override to name each instance in the database
    def __str__(self):
        return f"{self.title}"
