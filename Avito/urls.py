"""Avito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from ads.views.service import health_check
from ads.views import ads as ads_view
from ads.views import category as cat_view
from ads.views import users as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', health_check),

    path('cat/', cat_view.CategoryListView.as_view()),
    path('cat/<int:pk>/', cat_view.CategoryDetailView.as_view()),
    path('cat/create/', cat_view.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', cat_view.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', cat_view.CategoryDeleteView.as_view()),

    path('ad/', ads_view.AdListView.as_view()),
    path('ad/<int:pk>/', ads_view.AdDetailView.as_view()),
    path('ad/crate/', ads_view.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', ads_view.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', ads_view.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', ads_view.AdUploadImageView.as_view()),
    path('user/', users_view.UserListView.as_view())
]
