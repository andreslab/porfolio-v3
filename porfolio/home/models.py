from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    phone = models.CharField(max_length=9)
    email = models.EmailField(max_length=200)
    github = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    msg = models.CharField(max_length=800)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email