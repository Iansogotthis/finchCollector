from django.shortcuts import render

# Create your views here.

#The Home View
# Define the home view
def home(request):
  return render(request, 'home.html')