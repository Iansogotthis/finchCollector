from django.shortcuts import render

def home(request):
    finch_data = [
        {'name': 'House Finch', 'color': 'Red', 'habitat': 'Urban areas'},
        {'name': 'Goldfinch', 'color': 'Yellow', 'habitat': 'Open fields and meadows'},
        # Add more finch data as needed
    ]
    return render(request, 'templates/home.html', {'finch_data': finch_data})

from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')