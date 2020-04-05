from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:locale_name>/', views.index_locale, name='locale'),
    path('<str:locale_name>/<str:section_name>/', views.index_section, name='section'),
    path('<str:locale_name>/<str:section_name>/<str:subsection_name>', views.index_subsection, name='subsection'),
    path('<str:classified.locale>/<str:classified.section_name>/<str:classified.subsection_name>/<int:classified_id>', views.detail, name='detail')
]
