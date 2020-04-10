from django.contrib import admin

# Register your models here.
from .models import Classified, Page, Locale, Section, Subsection

admin.site.register(Classified)
admin.site.register(Page)
admin.site.register(Locale)
admin.site.register(Section)
admin.site.register(Subsection)
