from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from publication.views import *
from django.contrib.auth import views as acc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publication.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('i18n/',include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('publication.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
urlpatterns += [
    path('accounts/login/',acc.LoginView.as_view(),name='login'),
    path('accounts/logout/',acc.LogoutView.as_view(),name='logout'),
    path('accounts/password-reset',acc.PasswordResetView.as_view(),name='password_reset'),
    path('accounts/password-change', acc.PasswordChangeView.as_view(),name='password_change'),
    path('signup/', signup, name='signup'),
    #path('accounts/', include('django.contrib.auth.urls')),
]'''