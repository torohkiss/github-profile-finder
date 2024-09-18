import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def user(request):
    # username = request.POST['username']
    # return render(request, 'user.html', {'username': username})
    if request.method == "POST":
        username = request.POST.get('username')
        response = requests.get(f'https://api.github.com/users/{username}')
        if response.status_code == 200:
            user_data = response.json()
            return render(request, 'user.html', {'user': user_data})
        else:
            return HttpResponse("User not found", status=404)
    else:
        return HttpResponse("Invalid request method", status=405)
