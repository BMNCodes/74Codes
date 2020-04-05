from django.urls import path
from . import views

#from django.contrib import admin
#from accounts.views import home_view, signup_view



urlpatterns=[
    path('', views.news_list, name= 'news_list'),
    path('<int:year>/<int:month>/<int:day>/<str:news>/',views.news_detail, name= 'news_detail'),

#    path('admin/', admin.site.urls),
#    path('', home_view, name="home"),
#    path('signup/', signup_view, name="signup")
]