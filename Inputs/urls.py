from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name='home'),
    path("inputsv1/", views.inputsv1, name='inputsv1'),
    path("inputsv3/", views.inputsv3, name='inputsv3'),
    # path("inputs/", views.inputs, name="inputs"),
    # path("results/", views.results, name="results"),
    path("resultsv1/", views.resultsv1, name="resultsv1"),
    path("resultsv3/", views.resultsv3, name="resultsv3"),
    # path("changes/", views.changes, name="changes"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),    
    # path("register/", views.registerPage, name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    