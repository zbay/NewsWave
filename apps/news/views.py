from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from .models import *

def start(request):
    init_session(request)
    if user_id != "":
        return redirect("/homepage")
    context = {
        'name': request.session['name'],
        'username': request.session['username']
    }
    return render(request, "start.html", context)

def login(request):
    init_session(request)
    if user_id != "" or request.method != "POST":
        return redirect("/homepage")
    login_result = User.objects.login(request.POST)
    errors = login_result['errors']
    request.session['username'] = request.POST['username']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = login_result['user'].id
        request.session['first_name'] = extract_first_name(login_result['user'].name)
        return redirect("/homepage")

def register(request):
    init_session(request)
    if user_id != "" or request.method != "POST":
        return redirect("/homepage")
    register_result = User.objects.register(request.POST)
    errors = register_result['errors']
    request.session['username'] = request.POST['username']
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        request.session['name'] = request.POST['name']
        return redirect("/")
    else:
        request.session['user_id'] = register_result['user'].id
        request.session['first_name'] = extract_first_name(login_result['user'].name)
        return redirect("/settings")

def logout(request):
    reset_session(request)
    return redirect("/")

def home(request):
    init_session(request)
    # get all locations, outlets, and notes connected to the specific user
    user = User.get(id=request.session['user_id'])
    locations = user.locations.all()
    outlets = user.outlets.all()
    notes = user.notes.all()
    context = {
        'first_name': request.session['first_name'],
        'locations': locations,
        'outlets': outlets,
        'notes': notes
    }
    return render(request, "home.html", context)

def get_news(request): # maybe do this 100% on the client side
    init_session(request)

def notes(request):
    init_session(request)
    # return all notes as JSON to the client using AJAX

def reading_list(request, username):
    init_session(request)
    stories = User.objects.get(id=request.session['user_id']).stories.all()
    context = {
        'stories': stories
    }
    return render(request, "reading_list.html", context)

def settings(request):
    init_session(request)
    # how do we display the saved settings?

def delete_story(request):
    init_session(request)
    

def new_note(request):
    init_session(request)

def delete_note(request):
    init_session(request)

def init_session(request):
    if not 'user_id' in request.session:
        reset_session(request)

def reset_session(request):
        request.session['user_id'] = ""
        request.session['name'] = ""
        request.session['username'] = ""
    
def extract_first_name(name):
    try:
        space_index = name.index(" ")
        if space_index > 0:
            return name[:space_index]
    except:
        pass
    return name