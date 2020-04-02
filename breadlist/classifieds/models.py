from django.db import models

class Classified(models.Model):
    classified_text = models.TextField()
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    time_created = models.TimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    locale = models.ForeignKey("the subbreadlist usually a city, eg chicago or twin cities", Locale, on_delete=models.CASCADE)
    section = models.CharField("section of the postings, eg water, food, shelter", max_length=40)
    narotype = models.CharField("needed, available, resource or organizations", max_length=40)

class User(models.Model):
    username = models.Charfield(max_length=16)

class Locale(models.Model):
    locale_name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.Charfield(max_length=200)
