from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.user_login,name='Login'),
    path('registration',views.user_registration,name='Registration'),
    path('afterlogin',views.login_success,name='AfterLogin'),
    path('logout',views.logout,name='Logout'),
    path('after_mask',views.mask_detect,name='After_Mask')

]
