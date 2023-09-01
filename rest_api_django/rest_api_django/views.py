from django.http import HttpResponse, JsonResponse
def homepage(request):
    print("Homepage")
    colors = [
        'red', 'blue', 'yellow', 'green'
    ]
    # return HttpResponse("Homepage")
    return JsonResponse(colors, safe=False)