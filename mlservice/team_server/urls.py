from django.conf.urls import url
from . import views
 
urlpatterns = [
    # ex: /team_server/
    url(r'^$',views.index, name = 'index'),
    # ex: /team_server/test_form
    url(r'^test_form/$', views.test_form, name='test_form'),
    # ex: /team_server/test_form2
    url(r'^test_form2/$', views.test_form2, name='test_form2'),
    # ex: /team_server/video_face_analysis
    url(r'^video_face_analysis/$', views.video_face_analysis, name='video_face_analysis'),




    # ex: /team_server/webcam
    url(r'^webcam/$', views.webcam, name='webcam'),
    # ex: /team_server/sending
    url(r'^sending/$', views.sending, name='sending'),
]




