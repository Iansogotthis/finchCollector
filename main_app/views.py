from django.shortcuts import render


finches = [
        {'name': 'House Finch', 'color': 'Red', 'habitat': 'Urban areas', 'age': 0},
        {'name': 'Goldfinch', 'color': 'Yellow', 'habitat': 'Open fields and meadows', 'age': 2},
        # Add more finch data as needed
    ]


from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })