from django.conf.urls import url 
from django.contrib import admin 

                                                                                
urlpatterns = [
    url(r'^$', include('qa.urls')),
    url(r'^login/', include('qa.urls')),
    url(r'^signup/', include('qa.urls')),
    url(r'^question/(\d+)/$', include('qa.urls')),
    url(r'^ask/', include('qa.urls')),
    url(r'^popular/', include('qa.urls')),
    url(r'^new/', include('qa.urls')),
    
]
