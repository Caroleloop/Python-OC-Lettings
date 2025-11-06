from django.shortcuts import render
from .models import Profile


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
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
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
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
