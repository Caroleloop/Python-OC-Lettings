from django.shortcuts import render
from logging_conf import sentry_log


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
    try:
        sentry_log("info", "Homepage accessed")
        return render(request, "index.html")
    except Exception as e:
        sentry_log("exception", f"Unexpected error rendering homepage: {e}")
        return render(request, "500.html", status=500)


def custom_404(request, exception):
    """
    Render the custom 404 error page.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: Rendered template '404.html' with status code 404.
    """
    sentry_log("warning", f"404 Not Found: {request.path}")
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Render the custom 500 error page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template '500.html' with status code 500.
    """
    sentry_log("exception", "500 Internal Server Error encountered")
    return render(request, "500.html", status=500)
