"""ePresenceServer URL Configuration

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
from django.conf.urls import url, include
from app import views
from app.resources import AulaResource

aula_resource = AulaResource()

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^home/', views.home, name='home'),
    path('admin/', admin.site.urls),
	url(r'^api/', include(aula_resource.urls)),
    url(r'^aula/(\d+)/$', views.aula, name='aula'),

    url(r'^aulaAdd/(\d+)/$', views.aula_p_add, name='aula_add'),
    url(r'^aulaRemove/(\d+)/$', views.aula_p_remove, name='aula_remove'),

    url(r'^aulaVerde/(\d+)/$', views.aula_e_verde, name='aula_s_verde'),
    url(r'^aulaAmarillo/(\d+)/$', views.aula_e_amarillo, name='aula_s_amarillo'),
    url(r'^aulaRojo/(\d+)/$', views.aula_e_rojo, name='aula_s_rojo'),

]
