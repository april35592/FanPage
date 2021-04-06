from django.urls import path
from . import views

app_name = 'works'
urlpatterns = [
    path('', views.workOverview, name='overview'),
    path('list/', views.workList, name='list'),
    path('detail/<str:pk>/', views.workDetail, name='detail'),
]