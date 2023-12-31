from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:id>/', views.room, name="room"),
    path('login', views.login, name="login")

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
