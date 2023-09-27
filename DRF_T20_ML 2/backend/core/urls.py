from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace="account")),
    path('', include('tournament.urls', namespace="tournament")),
    path('faq/', include('faq.urls', namespace="faq")),
    path('contactus/', include('contactus.urls', namespace="contactus")),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
