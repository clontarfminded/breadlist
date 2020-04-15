from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Locale, Section, Subsection
from classifieds.models import Classified

# class CreateClassifiedForm(forms.Form):
#     LOCALECHOICES = []
#     SECTIONCHOICES = []
#     SUBSECTIONCHOICES = []
#     locale_list = Locale.objects.order_by('locale_name')
#     section_list = Section.objects.order_by('pk')
#     subsection_list = Subsection.objects.order_by('pk')
#     for l in locale_list:
#         LOCALECHOICES.append((str(l), str(l)))
#     for s in section_list:
#         SECTIONCHOICES.append((str(s), str(s)))
#     for ss in subsection_list:
#         SUBSECTIONCHOICES.append((str(ss), str(ss)))
#     classified_title = forms.CharField(max_length=200)
#     classified_text = forms.CharField(max_length=20000)
#     locale = forms.TypedChoiceField(choices=LOCALECHOICES)
#     section = forms.ChoiceField(choices=SECTIONCHOICES)
#     subsection = forms.ChoiceField(choices=SUBSECTIONCHOICES)

class CreateClassifiedForm(ModelForm):
    class Meta:
        model = Classified
        fields = ['classified_title', 'classified_text', 'locale', 'section', 'subsection']
