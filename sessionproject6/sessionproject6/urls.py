from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.name_view, name='name_view'),
    path('age/', views.age_view, name='age_view'),
    path('gf/', views.gf_view, name='gf_view'),
    path('result/', views.result_view, name='result_view'),
]
