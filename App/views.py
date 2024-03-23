# Create your views here.
from django.shortcuts import render,redirect
# imported our models
from django.core.paginator import Paginator
from . models import Song



def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)

def aboutus(request):
   return render(request,"aboutus.html")

def contact(request):
   return render(request,"contact.html")

def playlist(request):
   songs = Song.objects.all()
   return render(request, 'playlist.html', {'songs': songs})


from django.shortcuts import render
from .models import Song

def playlist_view(request):
    # Fetch all songs from the database
    songs = Song.objects.all()
    return render(request, 'playlist.html', {'songs': songs})



from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignupForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                # Handle invalid login
                pass
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
