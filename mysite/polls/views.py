from polls.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Participant, Poll

from .forms import RegistrationForm


def index(request):
    # return HttpResponse("TEST")
    # 'all()' is getting all instances from database
    polls = Poll.objects.all()
    return render(request, "polls/index.html", {"polls": polls})


def polls_details(request, poll_slug):
    try:
        selected_poll = Poll.objects.get(slug=poll_slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            # validation check on the forms, if the form is invalid, django will save
            # the error in the form object as well so when returning the render template
            # the error will be shown in the page
            if registration_form.is_valid():
                # save a new entry to the model which the forms is based to the database
                # cleaned_data - dictionary holds data entered by user as key balue pairs in
                # dictionary so can access email
                user_email = registration_form.cleaned_data["email"]
                # _ is value of "was_created" get_or_create return tuple
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_poll.participant.add(participant)

                return redirect("confirm-registration", poll_slug=poll_slug)

        return render(
            request,
            "polls/poll_details.html",
            {"poll_found": True, "poll": selected_poll, "form": registration_form},
        )

    except Exception as e:
        # like 404 page for handling no such result
        print(e)
        return render(request, "polls/poll_details.html", {"poll_found": False})


def confirm_registration(request, poll_slug):
    try:
        selected_poll = Poll.objects.get(slug=poll_slug)
    except Exception as e:
        return render(request, "polls/poll_details.html", {"poll_found": False})

    return render(
        request,
        "polls/registration_success.html",
        {"organizer_email": selected_poll.organizer_email},
    )
