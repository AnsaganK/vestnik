from django.urls import path
from .views import *
from django.contrib.auth import views as acc



urlpatterns = [
    path('', index, name='about'),
    path('archive/',archive, name='archive'),
    path('<int:pk>/', detailPage, name='detailPage'),

    path('publications/',publications, name='publications'),
    path('publication/<int:pk>',publication, name='publication'),
    path('vestniks/',vestniks,name='vestniks'),
    path('publications/<int:pk>/',only_publication, name='only_publication'),
    path('add_file/',add_file, name='add_file'),
    path('add_vestnik/',add_vestnik, name='add_vestnik'),
  #  path('seria_detail/<int:pk>',seria_detail, name='seria_detail'),
    path('search',search,name='search'),
    path('cabinet',cabinet,name='cabinet'),
    path('filter/',filter_publications,name='filter'),
    #path('filter_ajax/',filter_ajax,name='filter_ajax'),
    path('update_redactor/<int:pk>',update_redactor,name='update_redactor'),
    path('update_antiplagiat/<int:pk>',update_antiplagiat,name='update_antiplagiat'),
    path('update_reviewer/<int:pk>',update_reviewer,name='update_reviewer'),
    path('update_profile/<int:pk>',update_profile,name='update_profile'),
    path('update_payload_img/<int:pk>',update_payload_img,name='update_payload_img'),
    path('all_publications/',get_all_publications,name='get_publications'),
    path('reprofile/',reprofile,name='reprofile'),
    path('reprofile_post/',view_reprofile,name='reprofile_post'),
    path('update_payload/<int:pk>',update_payload,name='update_payload'),
    path('update_file_redactor/<int:pk>',return_file_redactor,name='update_file_redactor'),
    path('update_file_reviewer/<int:pk>',return_file_reviewer,name='update_file_reviewer'),
    path('api/',api_file,name='api_file'),
]

urlpatterns += [
    path('accounts/login/',acc.LoginView.as_view(),name='login'),
    path('accounts/logout/',acc.LogoutView.as_view(),name='logout'),
    path('accounts/password-reset',acc.PasswordResetView.as_view(),name='password_reset'),
    path('accounts/password-change/done/', acc.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password-change', acc.PasswordChangeView.as_view(),name='password_change'),
    path('signup/', signup, name='signup'),
    #path('accounts/', include('django.contrib.auth.urls')),
]