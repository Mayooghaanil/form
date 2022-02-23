from django.urls import path
from first_app import views

app_name="first_app"

urlpatterns=[
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('about',views.about,name="about")
]