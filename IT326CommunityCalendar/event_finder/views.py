from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Max
from .forms import CEFForm, LoginForm,CreateEvent,EditEvent, CommentForm, RSVPForm, EditProfile,SearchForm
from .models import Users, Event, Comment, RSVP
from Utils import User_Account, User_Details, Contact_Info, Location
from datetime import datetime,timezone
from datetime import date

# Global User Variable to have a persistent User account
# user_details = User_Details.User_Details(["soccer", "cars"], ["soccer", "racing"], 21, "Male")
# user_location = Location.Location("user_from_db.user_street", "user_from_db.user_city", "user_from_db.user_state", "user_from_db.user_zipcode")
# user = User_Account.User_Account(0, "ewhazza", "rootuser", user_details)
# user_contact = Contact_Info.Contact_Info("Evan", "Hazzard", "ewhazza@ilstu.edu", 555555, user_location)
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
        'update': True
    }
    if(user):
        context['admin'] = user.is_admin
    return render(request, 'event_finder_base.html', context)


def event_search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if form['event_title'].value():
                event_list = Event.objects.filter(event_title=form['event_title'].value()).values()
            elif form['event_city'].value():
                event_list = Event.objects.filter(event_city=form['event_city'].value()).values()
            elif form['event_state'].value():
                event_list = Event.objects.filter(event_state=form['event_state'].value()).values()
            else:
                event_list = Event.objects.all().order_by('-event_date').values()
            context = {
                    'query' : event_list,
                    'user': user,
                    'form': form
            }
            return render(request, 'event_finder_base.html', context)
    return render(request,'event_search_form.html', {'form': form, 'user' : user})

def profile(request):
    numRSVPs = RSVP.objects.filter(user_id=user.user_id).count()
    user_obj = Users.objects.get(user_id=user.user_id)
    user_events = Event.objects.filter(user_id=user.user_id).values()
    user_rsvps = RSVP.objects.filter(user_id=user.user_id).values()
    context = {
        'user_query' : user_obj,
        'numrsvp' : numRSVPs,
        'updateaddress' : 'profileupdate/',
        'event_query' : user_events,
        'rsvp_query': user_rsvps,
        'user' : user,
        'new' : True,
        'newaddress' : 'eventcreate/',
        'delete': True,
        'userdeleteaddress': 'deleteuser/'
    }
    return render(request, 'profile_page.html', context)

def profileupdate(request):
    user_object = Users.objects.get(user_id=user.user_id)
    form = EditProfile(instance=user_object)
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=user_object)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = { 
               "form": form,
               "user": user
    }
    return render(request, 'edit_profile_form.html', context)


def eventcreate(request):
    # If there is a Event in the table already, increase the last ID by one and make the new comment id that new number
    if Event.objects.all().exists:
        new_event_id = Event.objects.latest('event_id').event_id + 1
    # If this is the first Event, ID = 0
    else:
        new_event_id = 0
    global user
    form = CreateEvent()
    print(type(user))
    if (type(user) != None):
        data = {
                'event_id': new_event_id,
                'user_id': user.user_id, 
                'event_email': user.contact_info.email,
                'event_phone': user.contact_info.phone,
                'event_city': user.contact_info.location.city,
                'event_state': user.contact_info.location.state,
                'event_date':  date.today(),
                'creator_first_name': user.contact_info.first_name,
                'creator_last_name': user.contact_info.last_name}
        form = CreateEvent(initial=data)
    else:
        redirect(login)
    if request.method == 'POST':
        form = CreateEvent(request.POST, initial=data)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {
            "form":form,
            "user": user
    }
    return render(request, 'create_event_form.html', context)


def create_account(request):
    # If there is a Users in the table already, increase the last ID by one and make the new comment id that new number
    if(Users.objects.all().exists()):
        new_user_id =  Users.objects.latest('user_id').user_id + 1
    # If this is the first User, ID = 0
    else:
        new_user_id = 0
    data = {'user_id': new_user_id}
    form = CEFForm(initial=data)
    if request.method == 'POST':
        # Add the request to a Users object
        form = CEFForm(request.POST, initial=data)
        # If the form is valid, save it
        if form.is_valid():
            form.save()
            # Return control to home page after form submission
            return redirect(home)
    context = {'form': form , 'user' : user}
    return render(request, 'create_account.html', context)

# View to facilitate the log in requirement
def login(request):
    # Uses the LoginForm to prompt the user for data and check if the password was entered correctly
    form = LoginForm()
    if request.method == 'POST':
        # get form object from user
        form = LoginForm(request.POST)
        # Scrape input from the form
        input_username = form['user_username'].value()
        input_password = form['user_password'].value()
        # Get the user object from the data that matches the input username
        # TODO surround with Try Catch to handle incorrect username
        user_from_db = Users.objects.get(user_username = input_username)
        # If the correct password was entered, scrape the data from the database and create a user and contact info object that are global variables
        if user_from_db.user_password == input_password:
            user_details = User_Details.User_Details(user_from_db.user_hobbies, user_from_db.user_interests, user_from_db.user_age, user_from_db.user_gender)
            user_location = Location.Location(user_from_db.user_street, user_from_db.user_city, user_from_db.user_state, user_from_db.user_zipcode)
            user_contact = Contact_Info.Contact_Info(user_from_db.user_fname, user_from_db.user_lname, user_from_db.user_email, user_from_db.user_phone, user_location)
            # To change the global version of the variables we have to address them as such
            global user
            user = User_Account.User_Account(user_from_db.user_id, user_from_db.user_username, user_from_db.user_password, user_details, user_from_db.user_admin, user_contact)
            # Redirect back to the homepage with logged in screen
            return redirect(home) 
        else:
            pass
            # Handle incorrect Login
    context = {'form': form, 'user' : user,}
    return render(request, 'login.html', context)

def update_event(request, event_id):
    event_object = Event.objects.get(event_id=event_id)
    form = EditEvent(instance=event_object)
    if request.method == 'POST':
        form = EditEvent(request.POST, instance=event_object)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = { 
               "form": form,
               "user": user
    }
    return render(request, 'edit_event_form.html', context)

def delete_event(request, event_id):
    Event.objects.get(event_id=event_id).delete()
    return redirect(home)

def event_landing_page(request, event_id):
    event_object = Event.objects.get(event_id=event_id)
    time_diff = str(event_object.event_date.replace(tzinfo=None) - datetime.now().replace(tzinfo=None))
    time_diff_ls = time_diff.split('.')
    time_diff = time_diff_ls[0]
    comments_object = Comment.objects.filter(event_id=event_id)
    rsvp_object = RSVP.objects.filter(event_id=event_id)
    context = {
        'countdown' : time_diff,
        'event_query' : event_object,
        'user' : user,
        'new' : True,
        'newcommentaddress': "comment",
        'comment_query': comments_object,
        'RSVP': True,
        'rsvpaddress': "rsvp",
        'rsvp_query': rsvp_object
    }
    return render(request, 'event_landing_page.html', context)

def add_comment(request, event_id):
    # If there is a comment in the table already, increase the last ID by one and make the new comment id that new number
    if(Comment.objects.all().exists()):
        new_comment_id = Comment.objects.latest('comment_id').comment_id + 1
    # If there exists no comments, make the ID 0
    else:
        new_comment_id = 0
    event_object = Event.objects.get(event_id=event_id)
    data = {'user_id': event_object.user_id, 
            'event_id': event_object.event_id,
            'comment_id': new_comment_id}
    form = CommentForm(initial = data)
    if request.method == 'POST':
        # Add the request to a Users object
        form = CommentForm(request.POST, initial = data)
        # If the form is valid, save it
        if form.is_valid():
            form.save()
            # Return control to home page after form submission
            return redirect(home)
    context = {'form': form, 'user': user}
    return render(request, 'add_comment.html', context)

def rsvp_to_event(request, event_id):
    event_object = Event.objects.get(event_id=event_id)
    if(RSVP.objects.all().exists()):
        rsvp_new_id = RSVP.objects.latest('rsvp_id').rsvp_id + 1
    else:
        rsvp_new_id = 0
    data = {'user_id': event_object.user_id, 
            'event_id': event_object.event_id,
            'rsvp_date': date.today(),
            'rsvp_id': rsvp_new_id }
    form = RSVPForm(initial = data)
    if request.method == 'POST':
        # Add the request to a Users object
        form = RSVPForm(request.POST, initial = data)
        # If the form is valid, save it
        if form.is_valid():
            form.save()
            # Return control to home page after form submission
            return redirect(home)
    context = {'form': form, 'user' : user, 'event_name': event_object.event_title}
    return render(request, 'add_rsvp.html', context)

def logout(request):
    global user, user_contact
    user = None
    user_contact = None
    return redirect(home)
        
def delete_rsvp(request, rsvp_id):
    RSVP.objects.get(rsvp_id=rsvp_id).delete()
    return redirect(home)

def delete_user(request, user_id):
    Users.objects.get(user_id=user_id).delete()
    global user
    user = None
    return redirect(home)
    