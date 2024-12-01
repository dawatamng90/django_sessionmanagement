from django.shortcuts import render
from testapp.forms import AddItemForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

def additem_view(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            # Extract cleaned data after validating the form
            itemname = form.cleaned_data['itemname']
            quantity = form.cleaned_data['quantity']

            # Create response and set cookie with the item details
            response = render(request, 'testapp/additem.html', {'form': form, 'success': True})
            response.set_cookie(itemname, quantity, 30)
            return response
    else:
        # For GET requests, show an empty form
        form = AddItemForm()
    
    return render(request, 'testapp/additem.html', {'form': form})


def display_view(request):
    return render(request,'testapp/displayitems.html')