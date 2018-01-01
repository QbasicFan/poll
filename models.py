from django.db import models
from django.utils import timezone
'''
 Create your models here.
This is where the poll models starts
goal :
Based on the poll apps
https://docs.djangoproject.com/en/2.0/intro/tutorial04/
modify it to make a quiz app
'''


class poll(models.Model):

    color = (
	    ("w3-red" , "Red"),
        ("w3-pink" , "Pink"),
        ("w3-purple" , "Purple"),
        ("w3-deep-purple" , "Deep Purple"),
        ("w3-indigo" , "Indigo"),
        ("w3-blue" , "Blue"),
        ("w3-light-blue" , "Light Blue"),
        ("w3-cyan" , "Cyan"),
        ("w3-aqua" , "Aqua"),
        ("w3-teal" , "Teal"),
        ("w3-green" , "Green"),
        ("w3-light-green" , "Light Green"),
        ("w3-lime" , "Lime"),
        ("w3-sand" , "Sand"),
        ("w3-khaki" , "Khaki"),
        ("w3-yellow" , "Yellow"),
        ("w3-amber" , "Amber"),
        ("w3-orange" , "Orange"),
        ("w3-deep-orange" , "Deep Orange"),
        ("w3-blue-grey" , "Blue Grey"),
        ("w3-brown" , "Brown"),
        ("w3-light-grey" , "Light Grey"),
        ("w3-grey" , "Grey"),
        ("w3-dark-grey" , "Dark Grey"),
        ("w3-pale-red" , "Pale Red"),
        ("w3-pale-yellow" , "Pale Yellow"),
        ("w3-pale-green" , "Pale Green"),
        ("w3-pale-blue" , "Pale Blue"),
         )



    title = models.CharField(max_length=400)
    menu = models.CharField(max_length=400 , choices=color)
    footer = models.CharField(max_length=400 , choices=color)
    body = models.CharField(max_length=400 , choices=color)
    votes = models.IntegerField(default=0)


    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



