from django.urls import path
from . import views
app_name='credentials'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login1/',views.login1,name='login1'),
    path('logout/',views.logout,name='logout'),
    path('dep_login',views.dep_login,name='dep_login'),
    path('dep_home/',views.dep_home,name='dep_home'),
    path('dep_logout/',views.dep_logout,name='dep_logout'),
    path('add_user/',views.add_user,name='add_user'), #add user for adding user from department
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('sadd_user/',views.sadd_user,name='sadd_user'), #add user for adding user from principal
    path('admin_manage_user/',views.admin_manage_user,name='admin_manager_user'),
    path('admin_delete_user/<int:id>',views.admin_delete_user,name='admin_delete_user'),
    path('dep_manage/',views.dep_manage,name='dep_manage'),
    path('dep_delete/<int:id>',views.dep_delete,name='dep_delete'),
    path('profile/',views.profile,name='profile'),




]
