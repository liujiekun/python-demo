from django.conf.urls import url 
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
 # 登录页面
  url(r'^login/$', LoginView.as_view(template_name='login.html'), 
 name='login'),
  url(r'^logout/$', views.logout_view, name='logout'),
  url(r'^register/$', views.register, name='register'),
]
