from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:classified_id>', views.detail, name='detail'),
    path('create-classified/', views.create_classified, name='create_classified'),
    path('thanks/', views.thanks, name='thanks'),
    path('pages/<str:page_name>/', views.page, name='page'),
    path('regions/<region_id>', views.region, name='region'),
    path('provinces/<province_id>', views.province, name='province'),
    path('<str:locale_name>/', views.locale_index, name='locale'),
    path('<locale>/<str:section>/', views.section_index, name='section'),
    path('<locale>/<str:section>/<str:subsection>', views.subsection_index, name='subsection'),
]
