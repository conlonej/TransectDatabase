from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^dbViz/', include('dbViz.urls')),
	url(r'^admin/', admin.site.urls),
]
