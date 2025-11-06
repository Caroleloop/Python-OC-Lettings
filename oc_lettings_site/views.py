from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper
# non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae
# erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor
# magna, non finibus neque cursus id.
def index(request):
    """
    Render the global homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template 'index.html'.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """
    Render the custom 404 error page.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: Rendered template '404.html' with status code 404.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Render the custom 500 error page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template '500.html' with status code 500.
    """
    return render(request, "500.html", status=500)
