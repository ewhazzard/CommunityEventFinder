from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'event_finder_base.html')

def event_search(request):
    return render(request, 'event_search_page.html')
