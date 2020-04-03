from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Classified

def index(request):
    latest_classified_list = Classified.objects.order_by('-datetime_created')[:5]
    template = loader.get_template('classifieds/index.html')
    context = {
        'latest_classified_list': latest_classified_list,
    }
    return HttpResponse(template.render(context, request))

def index_locale(request, locale_name):
    response = "hello, you're looking at the index for {}".format(locale_name)
    return HttpResponse(response)

def index_section(request, locale_name, section_name):
    response = "hello, you're looking at the index for {} in {}".format(section_name, locale_name)
    return HttpResponse(response)

def index_narotype(request, locale_name, section_name, narotype_name):
    response = "hello, you're looking at the index for {} of {} in {}".format(narotype_name, section_name, locale_name)
    return HttpResponse(response)

def classified_detail(request):
    response = "hello, you're looking at the detail page for {}".format(classified_title)
    return HttpResponse(response)
