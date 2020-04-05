from django.urls import path
from . import views


urlpatterns=[
    path('', views.news_list, name= 'news_list'),
    path('<int:year>/<int:month>/<int:day>/<str:news>/',views.news_detail, name= 'news_detail'),

]
