from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CEFForm, LoginForm,CreateEvent
from .models import Users, Event

# Create your views here.
def home(request):
    lastest_events_list = Event.objects.all().order_by('-event_date').values()
    context = {
        'query' : lastest_events_list,
        'new' : True,
        'newaddress' : 'eventcreate/',
        'delete': True,
        'deleteaddress': 'delete_event'
    }
    return render(request, 'event_finder_base.html', context)

def event_search(request):
    return render(request, 'event_search_page.html')

def profile(request):
    return render(request, 'profile_page.html')

def login(request):
    return render(request, 'login_page.html')

def eventcreate(request):
    form = CreateEvent()
    print(request.method)
    if request.method == 'GET':
        form = CreateEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_event_form.html',{"form":form})
    
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

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        # get form object from user
        form = LoginForm(request.POST)
        # Try to Get User object from input
        user = Users.objects.get(user_username = form['user_username'].value())
        if user.user_username == form['user_username'].value():
            return redirect('')
        else:
            pass
            # Handle incorrect Login
    context = {'form': form}
    return render(request, 'login.html', context)
