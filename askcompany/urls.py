from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

# icon create package
# ref = https://django-pydenticon.readthedocs.io/en/0.2/installation.html
# ref = https://github.com/azaghal/django-pydenticon/blob/master/django_pydenticon/urls.py
# import django_pydenticon.urls -> django 2버전에서 만들어 진거라 django-pydenticon views 참조 후 변경
from django_pydenticon.views import image as pydenticon_image 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',login_required(TemplateView.as_view(template_name='root.html')),name='root'),
    path('identicon/image/<path:data>/', pydenticon_image,name='pydenticon_image'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/',include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)