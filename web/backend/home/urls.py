from . import views
from django.urls import path

urlpatterns = [     
    #<--------- Authentication releted path / urls start here ------->
    path('login_user', views.login_user, name="login_user"),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('comingsoon',views.page_404,name='page_404'),
    path('profile',views.profile,name='profile'),
    path('resume/<str:file_id>',views.user_info,name='resume'),
    path('resume',views.user_info,name='resume'),
    path('map',views.maps,name='map'),
    
    # path('forgetpassword',views.forget_password,name='forget_password'),    
    #<-------- other path / urls end here ------->
    path('dashboard', views.dashboard, name='home'),
    path('', views.index, name='index'),
    
    ]