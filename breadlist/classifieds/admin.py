from django.contrib import admin

# Register your models here.
from .models import Classified, Locale, Section, Subsection

admin.site.register(Classified)
admin.site.register(Locale)
admin.site.register(Section)
admin.site.register(Subsection)
