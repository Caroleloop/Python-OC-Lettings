from django.http import HttpResponse
from logging_conf import sentry_log


def trigger_404(request):
    # Force un log 404 pour Sentry
    sentry_log("warning", "Test 404 triggered manually")
    return HttpResponse("404 test sent to Sentry")


def trigger_500(request):
    # Force un log exception pour Sentry
    try:
        1 / 0
    except Exception as e:
        sentry_log("exception", f"Test 500 triggered: {e}")
    return HttpResponse("500 test sent to Sentry")
