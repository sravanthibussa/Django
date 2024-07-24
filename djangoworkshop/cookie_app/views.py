from django.http import HttpResponse
# Create your views here.
def set_cookie(______):
    response=HttpResponse("Cookie Set!")
    response.set_cookie('username','sravanthi')
    return response
def get_cookie(request):
    username=request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello, {username}!")
       


