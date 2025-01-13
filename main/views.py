from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .config import SIDEBAR_ITEMS

# Create your views here.
def index(request):
    return render(request, "main/index.html")

@login_required
def dashboard_view(request, category=None):
    if category is None:
        category = "dashboard"

    usertype = get_user_type(request)

    # Map usertype to the corresponding template file for the given category
    usertype_template_map = {
        "student": f"main/student/{category}.html",
        "parent": f"main/parent/{category}.html",
        "teacher": f"main/teacher/{category}.html",
    }

    context = {
        "sidebar_items": SIDEBAR_ITEMS.get(usertype), # list of sidebar categories + the path to the icons
        "username": request.user.username,
        "selected": category, # the currently selected category
        "points": 488, # FIXME: example data
        "fname": "First", # FIXME: example data
        "lname": "Last", # FIXME: example data
    }
    if get_context(request, category) != None:
        context.update(get_context(request, category))

    return render(request, usertype_template_map.get(usertype), context)

def error_view(request):
    context = {
        "code": 404,
        "message": "page not found",
    }
    return render(request, "404.html", context)

# Get the context for each category
# TODO: add all the categories
def get_context(request, category):
    if category == "leaderboard":
        return {
            # FIXME: example leaderboard data. HAS to be sorted by points in descending order
            "leaderboard": [
                {'name': 'Liam', 'points': 500, 'user_id': 1}, # Also add 'user_id' as such
                {'name': 'Olivia', 'points': 496},
                {'name': 'Noah', 'points': 492},
                {'name': 'Samriddha', 'points': 488},
                {'name': 'Oliver', 'points': 484},
                {'name': 'Ava', 'points': 480},
                {'name': 'Elijah', 'points': 476},
                {'name': 'Niraj', 'points': 472},
                {'name': 'James', 'points': 468},
                {'name': 'Isabella', 'points': 464},
                {'name': 'William', 'points': 460},
                {'name': 'Mia', 'points': 456},
                {'name': 'Rasum', 'points': 452},
                {'name': 'Charlotte', 'points': 448},
                {'name': 'Lucas', 'points': 444},
                {'name': 'Amelia', 'points': 440},
                {'name': 'Henry', 'points': 436},
                {'name': 'Harper', 'points': 432},
                {'name': 'Theodore', 'points': 428},
                {'name': 'Evelyn', 'points': 424},
                {'name': 'Jack', 'points': 420},
                {'name': 'Abigail', 'points': 416},
                {'name': 'Levi', 'points': 412},
                {'name': 'Ella', 'points': 408},
                {'name': 'Alexander', 'points': 404},
                {'name': 'Elizabeth', 'points': 400},
                {'name': 'Jackson', 'points': 396},
                {'name': 'Camila', 'points': 392},
                {'name': 'Sebastian', 'points': 388},
                {'name': 'Luna', 'points': 384},
                {'name': 'Mateo', 'points': 380},
                {'name': 'Sofia', 'points': 376},
                {'name': 'Daniel', 'points': 372},
                {'name': 'Avery', 'points': 368},
                {'name': 'Michael', 'points': 364},
            ]
        }

# returns the usertype of the user as a string
def get_user_type(request):
    user = User.objects.get(id=request.user.id)

    if hasattr(user, "student"):
        return "student"
    if hasattr(user, "parent"):
        return "parent"
    if hasattr(user, "teacher"):
        return "teacher"
    return "unknown"