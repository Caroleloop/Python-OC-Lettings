from django.shortcuts import render, get_object_or_404
from .models import Letting
from logging_conf import sentry_log
from django.http import Http404


def lettings_index(request):
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template 'lettings/index.html' with context
        containing all Letting instances.

    Context:
        lettings_list (QuerySet[Letting]): A queryset of all lettings in the database.
    """

    try:
        lettings_list = Letting.objects.all()
        sentry_log("info", f"{lettings_list.count()} lettings fetched successfully")
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/index.html", context)
    except Exception as e:
        sentry_log("exception", f"Error fetching lettings list: {e}")
        context = {"lettings_list": []}
        return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display details for a specific letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: Rendered template 'lettings/letting.html' with context
        containing the title and address of the requested letting.

    Context:
        title (str): Title of the letting.
        address (Address): Related Address instance of the letting.

    Raises:
        Letting.DoesNotExist: If no Letting with the given ID exists.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        sentry_log("info", f"Letting fetched successfully: ID {letting_id}")
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Http404:
        sentry_log("warning", f"Letting not found: ID {letting_id}")
        return render(request, "404.html", status=404)
    except Exception as e:
        sentry_log(
            "exception", f"Unexpected error fetching letting ID {letting_id}: {e}"
        )
        return render(request, "500.html", status=500)
