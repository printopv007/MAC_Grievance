from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('add/',views.add,name='add'),
    path('view/',views.view,name='view'),
    path('feed/',views.feed,name='feed'),
    path('admin_view/',views.admin_view,name='admin_view'),
    path('admin_feed_view/',views.admin_feed_view,name='admin_feed_view'),
    #path('mca_view/',views.mca_view,name='mca_view'),
    #path('mba_view/',views.mba_view,name='mba_view'),
    path('dep_grieve_view/',views.dep_grieve_view,name='dep_grieve_view'),
    path('dep_feed_view/',views.dep_feed_view,name='dep_feed_view'),

]