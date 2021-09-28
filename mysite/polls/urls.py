from django.urls import path

from . import views

# must be urlpatterns, django will find path belong to this variable
urlpatterns = [
    path("", views.index, name="all-polls"),  # our-domain.com/polls
    path(
        "<slug:poll_slug>/success",
        views.confirm_registration,
        name="confirm-registration",
    ),
    path(
        "<slug:poll_slug>", views.polls_details, name="poll-detail"
    ),  # our-domain.com/polls/<dynamic>
]
