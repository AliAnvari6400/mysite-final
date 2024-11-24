from django.urls import path
from .views import login_view,logout_view,signup_view,reset_view,change_view

app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('signup/',signup_view,name='signup'),
    path('reset/',reset_view,name='reset'),
    path('change/',change_view,name='change')
]