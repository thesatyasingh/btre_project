from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices
    }
    return render(request, 'pages/index.html',context)

def about(request):
    realtors=Realtor.objects.order_by("-hire_date")
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    context={'realtors':realtors,'mvp_realtors':mvp_realtors}
    return render(request, 'pages/about.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {'listing':listing}
    return render(request, 'listings/listing.html', context)

def register(request):
    return render(request, 'pages/register.html')

def login(request):
    return render(request, 'pages/login.html')