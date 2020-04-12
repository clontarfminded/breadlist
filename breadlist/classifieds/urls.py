from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('pages/<str:page_name>/', views.page, name='page'),
    path('regions/<str:region_name>', views.region, name='region'),
    path('provinces/<str:province_name>', views.province, name='province'),
    path('<locale>/', views.locale_index, name='locale'),
    path('<locale>/<str:section>/', views.section_index, name='section'),
    path('<str:locale__abbreviation>/<str:section>/<str:subsection>', views.subsection_index, name='subsection'),
    path('<str:locale.abbreviation>/<str:section>/<str:subsection>/<int:classified__id>', views.detail, name='detail'),

]
