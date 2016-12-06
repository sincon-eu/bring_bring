from django.conf.urls import url, include

from LTE_HWMM.core import views

urlpatterns = [
    url(r'$', views.render_index)
]