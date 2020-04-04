from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Classified

def index(request):
    latest_classified_list = Classified.objects.order_by('-datetime_created')[:5]
    context = {
        'latest_classified_list': latest_classified_list,
    }
    return render(request, 'classifieds/index.html', context)

def index_locale(request, locale_name):
    response = "hello, you're looking at the index for {}".format(locale_name)
    return HttpResponse(response)

def index_section(request, locale_name, section_name):
    response = "hello, you're looking at the index for {} in {}".format(section_name, locale_name)
    return HttpResponse(response)

def index_narotype(request, locale_name, section_name, narotype_name):
    response = "hello, you're looking at the index for {} of {} in {}".format(narotype_name, section_name, locale_name)
    return HttpResponse(response)

def classified_detail(request, locale_name, section_name, narotype_name, classified_id):
    context = {
        'locale_name': locale_name,
        'section_name': section_name,
        'narotype_name': narotype_name,
        'classified_id': classified_id
    }
    return render(request, 'classifieds/detail.html', context)
