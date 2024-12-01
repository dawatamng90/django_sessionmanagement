from django.shortcuts import render, redirect
from testapp.forms import NameForm, AgeForm, GfForm

def name_view(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            return redirect('age_view')  # Redirect to the age view
    else:
        form = NameForm()
    return render(request, 'testapp/name.html', {'form': form})


def age_view(request):
    if 'name' not in request.session:
        return redirect('name_view')  # Redirect if session data is missing

    if request.method == "POST":
        form = AgeForm(request.POST)
        if form.is_valid():
            request.session['age'] = form.cleaned_data['age']
            return redirect('gf_view')  # Redirect to the girlfriend view
    else:
        form = AgeForm()
    return render(request, 'testapp/age.html', {'form': form, 'name': request.session['name']})

def gf_view(request):
    if 'age' not in request.session:
        return redirect('age_view')  # Redirect if previous session data is missing

    if request.method == "POST":
        form = GfForm(request.POST)
        if form.is_valid():
            # Save girlfriend's name in the session
            request.session['gfname'] = form.cleaned_data['gfname']
            return redirect('result_view')  # Redirect to the result page
    else:
        form = GfForm()
    return render(request, 'testapp/gf.html', {'form': form, 'name': request.session['name']})



def result_view(request):
    # Ensure all session data is present
    if 'name' not in request.session or 'age' not in request.session or 'gfname' not in request.session:
        return redirect('name_view')  # Redirect to the start if session data is missing

    # Retrieve data from the session
    name = request.session.get('name')
    age = request.session.get('age')
    gfname = request.session.get('gfname')

    # Render the result page with session data
    return render(request, 'testapp/result.html', {'name': name, 'age': age, 'gfname': gfname})
