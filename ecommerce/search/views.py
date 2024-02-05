from django.shortcuts import render

from django.db.models import Q

from shop.models import Product

# Create your views here.
def search(request):
    query = ""
    p = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query):
            products =Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))

    return render(request, 'search.html', {'query': query, 'p': products})