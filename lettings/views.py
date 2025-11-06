from django.shortcuts import render, get_object_or_404
from .models import Letting


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
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
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
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
