from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:locale_name>/', views.index_locale, name='locale'),
    path('<str:locale_name>/<str:section_name>/', views.index_section, name='section'),
    path('<str:locale_name>/<str:section_name>/<str:narotype_name>', views.index_narotype, name='narotype'),
    path('<str:locale_name>/<str:section_name>/<str:narotype_name>/<int:classified_id>', views.classified_detail, name='detail')
]
