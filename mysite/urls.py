from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('', include('notetake.urls'))
]
