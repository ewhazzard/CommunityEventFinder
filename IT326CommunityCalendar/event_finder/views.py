from django.shortcuts import render
from .forms import CEFForm

# Create your views here.
def home(request):
    return render(request, 'event_finder_base.html')

def event_search(request):
    return render(request, 'event_search_page.html')

def profile(request):
    return render(request, 'profile_page.html')

def login(request):
    return render(request, 'login_page.html')

def create_account(request):
    form = CEFForm()
    if request.method == 'POST':
        # Add the request to a Users object
        form = CEFForm(request.POST)
        # If the form is valid, save it
        if form.is_valid():
            form.save()
            # Return control to home page after form submission
            return redirect('home')
    context = {'form': form}
    return render(request, 'create_account.html', context)
