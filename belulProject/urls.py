"""belul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib.flatpages.views import *
from . import views

admin.site.site_header = settings.ADMIN_SITE_HEADER



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.mainView, name='mainPage'),
    url(r'^', include('connect.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^company/about/', flatpage, {'url':'/company/about/'}, name='about'),
    url(r'^company/goods/', flatpage, {'url':'/company/goods/'}, name='goods'),
    url(r'^company/park/', flatpage, {'url':'/company/park/'}, name='avtopark'),
    url(r'^stations/adresses/', flatpage, {'url':'/stations/adresses/'}, name='adresa'),
    url(r'^stations/services/', flatpage, {'url':'/stations/services/'}, name='uslugi'),
    url(r'^sale/conditionterms/', flatpage, {'url':'/sale/conditionterms/'}, name='postavka'),
    url(r'^sale/shipping/', flatpage, {'url':'/sale/shipping/'}, name='dostavka'),
    url(r'^contacts/', flatpage, {'url':'/contacts/'}, name='contacts'),
    url(r'^', include('article.urls')),
    url(r'^', include('price.urls')),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# /venv/lib/python2.7/site-packages/django/contrib/admin/static/admin