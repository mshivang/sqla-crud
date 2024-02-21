from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from chatplus.views import CustomVerifyEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include("users.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', CustomVerifyEmailView.as_view(), name='account_confirm_email'),
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
