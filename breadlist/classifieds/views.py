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

def index_locale(request, locale_id):
    locale = get_object_or_404(Locale, pk=locale_id)
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    context = {
        'locale': locale,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list
    }
    return render(request, 'classifieds/locale-index.html', context)

def index_section(request, locale_id, section_id):
    response = "hello, you're looking at the index for {} in {}".format(section_id, locale_id)
    return HttpResponse(response)

def index_subsection(request, locale_id, section_id, subsection_id):
    response = "hello, you're looking at the index for {} of {} in {}".format(subsection_id, section_id, locale_id)
    return HttpResponse(response)

def detail(request, classified_id):
    classified = get_object_or_404(Classified, pk=classified_id)
    return render(request, 'classifieds/detail.html', {'classified': classified})
