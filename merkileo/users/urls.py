from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/', registrartion_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/', delete_user, name='delete'),
    path('profile/', profile_page, name='profile'),
    path('profile/edit/', edit_profile_page, name='editProfile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
