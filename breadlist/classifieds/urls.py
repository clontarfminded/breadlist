from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('pages/<str:page_name>/', views.page, name='page'),
    path('<str:locale>/', views.locale_index, name='locale'),
    path('<str:locale>/<str:section>/', views.section_index, name='section'),
    path('<str:locale>/<str:section>/<str:subsection>', views.subsection_index, name='subsection'),
    path('<str:locale>/<str:section>/<str:subsection>/<int:classified_id>', views.detail, name='detail'),

]
