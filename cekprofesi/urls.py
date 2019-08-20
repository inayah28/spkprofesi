from django.conf.urls import url
from . import views
urlpatterns=[
# r=row
    url(r'^$',views.index),
    #url(r'^help/',views.help),
    # url(r'^profesi/',views.profesi),

    
]