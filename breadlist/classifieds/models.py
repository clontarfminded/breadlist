from django.db import models
from django.utils import timezone

class Locale(models.Model):
    locale_name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)
    def __str__(self):
        return self.locale_name

class Sublocale(models.Model):
    sublocale_name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=8)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    timezone = models.CharField(max_length=200)
    parent_locale = models.ForeignKey('Locale', on_delete=models.CASCADE)

    def __str__(self):
        return self.sublocale_name

class Section(models.Model):
    section_name = models.CharField(max_length=200)
    def __str__(self):
        return self.section_name

class Subsection(models.Model):
    subsection_name = models.CharField(max_length=200)
    def __str__(self):
        return self.subsection_name

class Classified(models.Model):
    classified_title = models.CharField(max_length=200)
    classified_text = models.TextField()
    datetime_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    locale = models.ForeignKey('Locale', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    subsection = models.ForeignKey('subsection', on_delete=models.CASCADE)
    def __str__(self):
        return self.classified_title
    def was_created_recently(self):
        return self.datetime_created >= timezone.now() - datetime.timedelta(days=1)
