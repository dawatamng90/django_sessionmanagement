from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    request.session.set_expiry(10)  # Set expiry to 10 seconds

    return render(request, 'testapp/pagecount.html', {'count': count})
