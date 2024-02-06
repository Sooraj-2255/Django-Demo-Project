from django.shortcuts import render

from netflix.forms import movieform

# Create your views here.
def home(request):
    return render(request,'base.html')

def addmovies(request):
    if request.method == 'POST':
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    else:
        form = movieform()

    return render(request, 'addmovie.html', {'form': form})