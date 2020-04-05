from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Classified, Locale, Section, Subsection

def index(request):
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    context = {
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list
    }
    return render(request, 'classifieds/index.html', context)

def index_locale(request, locale_name):
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    context = {
        'locale_name': locale_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list
    }
    return render(request, 'classifieds/locale-index.html', context)

def index_section(request, locale_name, section_name):
    section_classified_list = Classified.objects.filter(locale__locale_name=locale_name).filter(section__section_name=section_name).order_by('datetime_created')
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    context = {
        'locale_name': locale_name,
        'section_name': section_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'section_classified_list': section_classified_list
    }
    return render(request, 'classifieds/section-index.html', context)

def index_subsection(request, locale_name, section_name, subsection_name):
    response = "hello, you're looking at the index for {} of {} in {}".format(subsection_name, section_name, locale_name)
    return HttpResponse(response)

def detail(request, classified_id):
    classified = get_object_or_404(Classified, pk=classified_id)
    return render(request, 'classifieds/detail.html', {'classified': classified})
