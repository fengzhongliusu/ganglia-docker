from django.conf.urls import patterns, url
from ganglia import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),	
	url(r'^host(?P<host_id>\d+)/$', views.host_info, name='host_info'),
	url(r'^host(?P<host_id>\d+)/res(?P<resource_id>\d+)/$', views.res_info, name='res_info'),
    url(r'^log/$', views.all_log, name='log_page'),
    url(r'^xml/(?P<host_name>\S+)/(?P<rrd_name>\w+)/(?P<time_slot>\d+)/$', views.get_text),
    url(r'^last_update/(?P<host_name>\S+)/$', views.last_update),
    url(r'^last_mtc_avg/(?P<rrd_name>\w+)/$', views.last_mtc_avg),
    url(r'^hour_mtc_avg/(?P<rrd_name>\w+)/$', views.hour_mtc_avg),
    url(r'^get_log/$', views.get_log),
    url(r'^alert_post/$', views.deal_log),
    url(r'^coreos-host/$', views.coreos_host, name='coreos-host'),
    url(r'^deploy/$', views.deploy_app, name='deploy-app')
)
