from django.urls import path
from users import views
urlpatterns = [
    path('login',views.loginView,name='Login') ,   # login page path
    path('About',views.About,name='About'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('Identify',views.Identify,name='Identify'),
    path('Home',views.Home,name='Home'),
    path('Profile',views.Profile),
    path('UserView',views.UserView.as_view())         # as_view() because we use a class for viewing a page
]