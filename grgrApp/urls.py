from django.conf.urls import url
from grgrApp import views

urlpatterns = [
    url(r"^summary/$",views.summary_view,name='summary'),
    url(r"^stormwater/$",views.stormwater_view,name='stormwater'),
    url(r"^traffic/$",views.traffic_view,name='traffic'),
    url(r"^parameter/$",views.parameter_view,name='parameter'),
    url(r"^project/$",views.project_view,name='project'),
    url(r"^loginerror/$",views.login_view,name='loginerror'),
    url(r"^users/$",views.users_view, name='users'),
    url(r"^thanks/$",views.registration_view, name='thanks'),
    url(r"^logout/$",views.logout_view, name='logout'),
    url(r"^login/$",views.login_view, name='login'),
    url(r"^registration/$",views.registration_view, name='registration'),
    url(r"^$",views.index_view, name='index'),
]
