from django.conf.urls import url 
from . import views

urlpatterns = [
    # ex: /numberOracle/
    url(r'^$',views.index, name = 'index'),
    # ex: /numberOracle/oracle_handwritten.html/
    url(r'^oracle_handwritten/$', views.oracle_handwritten, name='oracle_handwritten'),
    # ex: /numberOracle/ajaxform/
    url(r'^ajaxform/$', views.ajaxform, name='ajaxform'),
    # ex: /numberOracle/oracleNumber/
    url(r'^oracleNumber/$', views.oracleNumber, name='oracleNumber'),



]



