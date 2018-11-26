from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "Hello, world. This our first page, we really need to hurry up"
    )
