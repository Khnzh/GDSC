from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('registration/', views.registration_request, name='registration'),
    path('tours/', views.ToursListView.as_view(), name='tours'),
    path('guides/', views.GuidesListView.as_view(), name='guides'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
    # path("songs/", views.songs, name="songs"),
    # path("photos/", views.photos, name="photos"),
    # path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    # path("signup/", views.signup, name="signup"),
    # path("concert/", views.concerts, name="concerts"),
    # path("concert-detail/<int:id>", views.concert_detail, name="concert_detail"),
    # path("concert_attendee/", views.concert_attendee, name="concert_attendee"),
]