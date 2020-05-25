"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('new/', views.new, name='new'),
    path('detail/<int:pk_select>', views.detail, name='detail'),
    path('delete/<int:pk_select>',views.delete, name='delete'),
    path('edit/<int:pk_select>',views.edit, name='edit'),
    path('delete_comment/<int:pk_select>/<int:pk_select_comment>',views.delete_comment, name='delete_comment')
]
