from django.shortcuts import render

# Create your views here.

def index(request):
    usernames = ["Erlan", "Arman", "Usman"]
    return render(request, 'main/index.html', {"names": usernames})