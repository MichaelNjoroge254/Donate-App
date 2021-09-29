from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "pk_test_51JewftKiPqgIMaeldN3qJqcNBDGJpk1u875J1VpeuZ0gJBI3h02vEcjh6kmXR03RrUjXDeutNh6TyARNyeWDVw4N00AfW9vOZg"

# Create your views here.

def index(request):
    return render(request, 'base/index.html')


def charge(request):
    amount = 5000
    if request.method == 'POST':
        print('Data:', request.POST)

        stripe

    return redirect(reverse('success', args=[amount])) 


def successMsg(request, args):
    amount = args
    return render(request, 'base/success.html', {'amount':amount})       


