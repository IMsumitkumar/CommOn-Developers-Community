from django.contrib import admin
from django.urls import path, include
from . import views
from common_app import views as common_views
from django.contrib.auth import views as auth_views
from common_app.forms import CustomAuthForm
from django.conf.urls.static import static
from user_profile import views as user_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',common_views.homepage, name='home'),

    path('login/',auth_views.LoginView.as_view(template_name="common_app/auth_login.html", authentication_form=CustomAuthForm), name='login'),
    path('register/',common_views.UserRegister.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='common_app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='common_app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='common_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='common_app/password_reset_complete.html'), name='password_reset_complete'),

    path('notes/',include("notes.urls", namespace='notes')),
    path('profile/',include("user_profile.urls", namespace='profile')),
    path('st_gp/', include("student_gp.urls", namespace='st_gp')),

    path('api/', include('qna.urls')),
    path('ug_api/',include('user_group.urls', namespace='ug_api')),
    path('askforteam/',include('recruit_team.urls')),

    path('myproject/',include('project_management.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# google serving media static during development django
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



# Submit email form                                 // PasswordResetView.as_view()
# Email sent succes message                         // PasswordResetDoneView.as_view()
# sent link to password reset from in Email         // PasswordResetConfirmView
# password successfully changed message             // PasswordResetCompleteView




