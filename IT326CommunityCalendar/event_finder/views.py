from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CEFForm, LoginForm,CreateEvent
from .models import Users, Event
from Utils import User_Account, User_Details, Contact_Info, Location

# Global User Variable to have a persistent User account
# user_details = User_Details.User_Details(["soccer", "cars"], ["soccer", "racing"], 21, "Male")
# user = User_Account.User_Account(0, "ewhazza", "rootuser", user_details)
user = None
user_contact = None

# Create your views here.
def home(request):
    lastest_events_list = Event.objects.all().order_by('-event_date').values()
    context = {
        'query' : lastest_events_list,
        'user' : user,
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
    if request.method == 'GET':
        form = CreateEvent(request.POST, initial={'user_id': user.user_id, 
                                                  'event_email': user_contact.email,
                                                  'event_phone': user_contact.phone,
                                                  'event_city': user_contact.city,
                                                  'event_state': user_contact.state})
        context = {
            "form":form,
            "user": user
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_event_form.html', context)
    
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
        input_username = form['user_username'].value()
        input_password = form['user_password'].value()
        user_from_db = Users.objects.get(user_username = input_username)
        print(user_from_db.user_username)
        if user_from_db.user_password == input_password:
            user_details = User_Details.User_Details(user_from_db.user_hobbies, user_from_db.user_interests, user_from_db.user_age, user_from_db.user_gender)
            user_location = Location.Location(user_from_db.user_street, user_from_db.user_city, user_from_db.user_state, user_from_db.user_zipcode)
            user_contact = Contact_Info.Contact_Info(user_from_db.user_fname, user_from_db.user_lname, user_from_db.user_email, user_from_db.user_phone, user_location)
            user = User_Account.User_Account(user_from_db.user_id, user_from_db.user_username, user_from_db.user_password, user_details)
            return redirect(home) 
        else:
            pass
            # Handle incorrect Login
    context = {'form': form}
    return render(request, 'login.html', context)
