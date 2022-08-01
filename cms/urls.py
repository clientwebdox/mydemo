"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import code

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import *
from blog2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about-us/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('post/<int:pk>', post, name="post"),
    path('post/create/', createpost, name="createpost"),
    path('editpost/<int:pk>', editpost, name="editpost"),
    path('about2/', about2, name="about2"),
    # path('code/', code, name="code")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)