from django.contrib import admin
from django.urls import path

from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
]