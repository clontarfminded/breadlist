from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Classified, Page, Locale, Section, Subsection

def index(request):
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list
    }
    return render(request, 'classifieds/index.html', context)

def locale_index(request, locale_name):
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_name': locale_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list
    }
    return render(request, 'classifieds/locale-index.html', context)

def section_index(request, locale_name, section_name):
    section_classified_list = Classified.objects.filter(locale__locale_name=locale_name).filter(section__section_name=section_name).order_by('datetime_created')
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_name': locale_name,
        'section_name': section_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'section_classified_list': section_classified_list
    }
    return render(request, 'classifieds/section-index.html', context)

def subsection_index(request, locale_name, section_name, subsection_name):
    subsection_classified_list = Classified.objects.filter(locale__locale_name=locale_name).filter(section__section_name=section_name).filter(subsection__subsection_name=subsection_name).order_by('datetime_created')
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_name': locale_name,
        'section_name': section_name,
        'subsection_name': subsection_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'subsection_classified_list': subsection_classified_list
    }
    return render(request, 'classifieds/subsection-index.html', context)

def detail(request, classified_id):
    classified = get_object_or_404(Classified, pk=classified_id)
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'classified': classified,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
    }
    return render(request, 'classifieds/detail.html', context)

def page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    locale_list = Locale.objects.order_by('pk')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    context = {
        'page': page,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
    }
    return render(request, 'classifieds/page.html', context)

def create_classified(request):
    pass
