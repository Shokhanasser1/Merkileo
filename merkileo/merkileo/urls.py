from django.contrib import admin
from django.urls import path, include
from .views import MainView, AboutPage
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('about/', AboutPage, name='aboutPage'),
]
