"""
URL configuration for api_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from posts.views import PostAPIDestroy, PostAPIUpdate, PostAPIList,PostLikeView,AnalyticView,LastLogin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', PostAPIList.as_view()),
    path('api/post/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/post/<int:pk>/like/', PostLikeView.as_view()),
    path('api/post_delete/<int:pk>/', PostAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/analytics/', AnalyticView.as_view()),
    path('last/', LastLogin.as_view()),

]
