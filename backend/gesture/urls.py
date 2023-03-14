from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('register_test/', views.register_test),
    path('login_test/', views.login_test),
    path('model_test/', views.hand_model),
    path('word_test/',views.change_word),
    path('proficiency_test/',views.change_proficiency),
    path('send_words/', views.send_words),
    path('get_words/', views.get_all_item),
]