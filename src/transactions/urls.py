from django.conf.urls import url
from transactions import views


urlpatterns = [
    url(r'^transactions/$',views.transaction_list),
    url(r'^transactions/(?P<pk>[0-9]+)/$', views.transaction_detail),   
]