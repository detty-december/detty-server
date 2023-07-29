"""
URL configuration for detty_server project.

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

from django.urls import path

from api.v1 import views

app_name = 'detty_server'

urlpatterns = [
    path('events/', views.EventView.as_view(), name='events'),
    path('business/events/', views.BusinessEventView.as_view(), name='business_events'),
    path('business/users/', views.BusinessUserView.as_view(), name='business_user'),
]
