from django.conf.urls import url
from . import views

urlpatterns = [
#test this !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    url(r'vote/(?P<pk>\d+)/$', views.vote, name='vote'),
    url(r'downVote/(?P<pk>\d+)/$', views.downVote, name='downVote'),

    url(r'testPage/(?P<pk>\d+)/$', views.testSite, name='testSite'),


    url(r'newPoll/$', views.newPoll, name='newPoll'),
    url(r'', views.index, name='index' ),

]
