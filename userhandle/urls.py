from django.urls import path 
from . import views , dashboard
from django.contrib.auth import views as auth_views


urlpatterns  = [
    path("", views.index, name="index"),
    path("user-login", views.user_login, name="login"),
    path("user-logout", views.user_logout, name="logout"),
    path('user-registration', views.user_register, name="registration"),
    path("about", views.about, name="about"), 
    path("contact", views.contact, name="contact"),
    
    # dashboard
    path("predict-weight", dashboard.rdkit_predict_mw, name="rdkit_predict_mw"),
    path("predict-hydrogen-bonds", dashboard.rdkit_predict_hydrogen, name="rdkit_predict_hydrogen"),
    path("predict-qsar", dashboard.deepchem_qsar, name="deepchem_qsar"),
    path("splicing", dashboard.splicing, name="splicing"),

    # genbank 
    path("genbank", views.genbank, name="genbank"),

    # deepchem
    # path("Solubility_prediction", dashboard.solubility_prediction, name='solubility-prediction'),

    # forgot password 
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password/enterEmail.html',
            email_template_name='password/password_reset_email.html',
            subject_template_name='password/password_reset_subject.txt'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password/recieveEmail.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password/enterNewPass.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]