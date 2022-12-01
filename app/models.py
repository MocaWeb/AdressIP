from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):



    name = models.CharField(max_length=100, null=False, blank=False)

    device_type = models.CharField(max_length=100, null=True, blank=False)
    browser_type = models.CharField(max_length=100, null=True, blank=False)
    browser_version = models.CharField(max_length=100, null=True, blank=False)
    os_type = models.CharField(max_length=100, null=True, blank=False)
    os_version = models.CharField(max_length=100, null=True, blank=False)
    location_country = models.CharField(max_length=100, null=True, blank=False)
    location_city = models.CharField(max_length=100, null=True, blank=False)


    timestamp = models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return self.name

    def __unicode__(self): 
        return self.name



    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'IP Adress'
        verbose_name_plural = 'IP Adresses'





class Link(models.Model):

    univ_choices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '14'),
    ('16', '15'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),                             
    ]

    url = models.URLField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    number = models.CharField(max_length=16, choices=univ_choices, null=True, blank=True)
    def __str__(self):
        return self.url

    def __unicode__(self): 
        return self.url



    class Meta:
       
        verbose_name = 'Link'
