from django.shortcuts import render
from .models import Finch

finches = [
        {'name': 'House Finch', 'color': 'Red', 'habitat': 'Urban areas', 'age': 0},
        {'name': 'Goldfinch', 'color': 'Yellow', 'habitat': 'Open fields and meadows', 'age': 2},
        # Add more finch data as needed
    ]



# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    # Fetch all Finch objects from the database
    finches = Finch.objects.all()
    
    # Create a list of dictionaries with required attributes including the database ID
    finch_data = []
    for finch in finches:
        finch_data.append({
            'id': finch.id,
            'name': finch.name,
            'color': finch.color,
            'habitat': finch.habitat,
            'age': finch.age
        })
    
    return render(request, 'finches/index.html', {
        'finches': finch_data
    })
def all_finches_view(request):
    finches = Finch.objects.all()
    return render(request, 'finches/all_finches.html', {'finch_data': finches})

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/finch_detail.html', { 'finch': finch })