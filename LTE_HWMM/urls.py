from django.conf.urls import url, include
from django.contrib import admin

from LTE_HWMM.core import urls as core_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$', include(core_urls))
]
