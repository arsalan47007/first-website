from django.urls import path

from checkins.views import home, get_form, report , aboutus,logout_confirm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home),
    path('add/', get_form),
    path('report/', report, name='report'),
    path('about/', aboutus ,name='about_us'),
#     path('logout/', auth_views.LogoutView.as_view(template_name="registration/logout_confirm"), name='logout'),
    path('logout/',logout_confirm)
]
