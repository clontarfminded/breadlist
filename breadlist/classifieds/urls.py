from django.urls import path

from . import views

app_name = "classifieds"
urlpatterns = [
    path('', views.index, name='index'),
    path('create-classified/', views.create_classified, name='create_classified'),
    path('thanks/', views.thanks, name='thanks'),
    path('pages/<str:page_name>/', views.page, name='page'),
    path('regions/<str:region_name>', views.region, name='region'),
    path('provinces/<str:province_name>', views.province, name='province'),
    path('<locale>/', views.locale_index, name='locale'),
    path('<locale>/<str:section>/', views.section_index, name='section'),
    path('<locale>/<str:section>/<str:subsection>', views.subsection_index, name='subsection'),
    path('<locale>/<str:section>/<str:subsection>/<int:classified__id>', views.detail, name='detail'),

]
