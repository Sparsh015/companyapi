from django.http import HttpResponse, JsonResponse

def home_page(request):
    friends = [
        "Alice", 
        "Bob", 
        "Charlie"
        ]
    return JsonResponse(friends, safe=False)
    # or -- return JsonResponse({'friends' : friends})
    

