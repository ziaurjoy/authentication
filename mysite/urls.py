
from django.contrib import admin
from django.urls import path,include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('signup', views.signup, name = 'signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
