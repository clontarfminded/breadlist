from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Classified, Page, Locale, Section, Subsection, Province, Region
from .forms import CreateClassifiedForm

def index(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/index.html', context)

def locale_index(request, locale_name):
    l = get_object_or_404(Locale, locale_name=locale_name)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale': l,
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/locale-index.html', context)

def section_index(request, locale, section):
    l = get_object_or_404(Locale, locale_name=locale)
    s = get_object_or_404(Section, section_name=section)
    section_classified_list = Classified.objects.filter(locale__locale_name=locale).filter(section__section_name=section).order_by('datetime_created')
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale': locale,
        'section': section,
        'page_list': page_list,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'section_classified_list': section_classified_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/section-index.html', context)

def subsection_index(request, locale, section, subsection):
    l = get_object_or_404(Locale, locale_name=locale)
    s = get_object_or_404(Section, section_name=section)
    ss = get_object_or_404(Subsection, subsection_name=subsection)
    subsection_classified_list = Classified.objects.filter(locale__locale_name=locale).filter(section__section_name=section).filter(subsection__subsection_name=subsection).order_by('datetime_created')
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page_list': page_list,
        'locale': locale,
        'section': section,
        'subsection': subsection,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'subsection_classified_list': subsection_classified_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/subsection-index.html', context)

def detail(request, classified_id):
    classified = get_object_or_404(Classified, pk=classified_id)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'classified': classified,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/detail.html', context)

def region(request, region_name):
    r = get_object_or_404(Region, region_name=region_name)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    province_list_sorted = Province.objects.filter(region__region_name=region_name).order_by('province_name')
    region_list = Region.objects.order_by('pk')
    context = {
        'page': page,
        'region_name': region_name,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
        'province_list_sorted': province_list_sorted,
    }
    return render(request, 'classifieds/region-index.html', context)

def province(request, province_name):
    p = get_object_or_404(Province, province_name=province_name)
    locale_list = Locale.objects.order_by('locale_name')
    locale_list_sorted = Locale.objects.filter(province__province_name=province_name).order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'province_name': province_name,
        'page': page,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
        'locale_list_sorted': locale_list_sorted
    }
    return render(request, 'classifieds/province-index.html', context)

def page(request, page_name):
    page = get_object_or_404(Page, page_name=page_name)
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'page': page,
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/page.html', context)

def thanks(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    context = {
        'locale_list': locale_list,
        'section_list': section_list,
        'subsection_list': subsection_list,
        'page_list': page_list,
        'province_list': province_list,
        'region_list': region_list,
    }
    return render(request, 'classifieds/thanks.html', context)

def create_classified(request):
    locale_list = Locale.objects.order_by('locale_name')
    section_list = Section.objects.order_by('pk')
    subsection_list = Subsection.objects.order_by('pk')
    page_list = Page.objects.order_by('pk')
    province_list = Province.objects.order_by('pk')
    region_list = Region.objects.order_by('pk')
    if request.method == 'POST':
        form = CreateClassifiedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = CreateClassifiedForm().as_ul()
        context = {
            'form': form,
            'locale_list': locale_list,
            'section_list': section_list,
            'subsection_list': subsection_list,
            'page_list': page_list,
            'province_list': province_list,
            'region_list': region_list,
        }
    return render(request, 'classifieds/create-classified.html', context)
