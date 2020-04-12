from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('pages/<str:page_name>/', views.page, name='page'),
    path('<locale>/', views.locale_index, name='locale'),
    path('<str:locale__abbreviation>/<str:section>/', views.section_index, name='section'),
    path('<str:locale__abbreviation>/<str:section>/<str:subsection>', views.subsection_index, name='subsection'),
    path('<str:locale.abbreviation>/<str:section>/<str:subsection>/<int:classified__id>', views.detail, name='detail'),

]
