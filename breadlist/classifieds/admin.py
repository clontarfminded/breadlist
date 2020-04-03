from django.contrib import admin

# Register your models here.
from .models import Classified, Locale, Section, Narotype

admin.site.register(Classified)
admin.site.register(Locale)
admin.site.register(Section)
admin.site.register(Narotype)
