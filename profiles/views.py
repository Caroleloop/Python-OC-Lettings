from django.shortcuts import render
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from logging_conf import sentry_log


def profiles_index(request):
    """
    Display a list of all user profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template 'profiles/index.html' with context
        containing all Profile instances.

    Context:
        profiles_list (QuerySet[Profile]): A queryset of all profiles in the database.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        sentry_log("info", f"{profiles_list.count()} profiles fetched successfully")
        return render(request, "profiles/index.html", context)
    except Exception as e:
        sentry_log("exception", f"Error retrieving profiles: {e}")
        context = {"profiles_list": []}
        return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Display details for a specific user profile.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: Rendered template 'profiles/profile.html' with context
        containing the requested Profile instance.

    Raises:
        Profile.DoesNotExist: If no Profile exists for the given username.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        sentry_log("info", f"Profile fetched for user: {username}")
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except ObjectDoesNotExist:
        sentry_log("warning", f"Profile not found for user: {username}")
        context = {"error": f"Profile for '{username}' does not exist."}
        return render(request, "profiles/profile.html", context)
    except Exception as e:
        sentry_log("exception", f"Unexpected error for user '{username}': {e}")
        context = {"error": "An error has occurred. Please try again later."}
        return render(request, "profiles/profile.html", context)
