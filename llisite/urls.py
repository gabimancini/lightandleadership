from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'', include('content.urls')),
]
=======
     url(r'', include('content.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
>>>>>>> upstream/master
