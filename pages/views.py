import json

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World!")


def pathView(request, count):
    return HttpResponse("Path request, count = " + count)  # чем отличается path от query?


def queryView(request):
    count = request.GET.get('count', None)
    return HttpResponse("Query request, count = " + count)


# curl --request POST \
#   --url http://127.0.0.1:8000/body/ \
#   --header 'Content-Type: application/json' \
#   --data '{"count":"6", "name":"Hello"}'
def bodyView(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        count = body['count']
        return HttpResponse(count)
