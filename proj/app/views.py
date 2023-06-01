from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, ReservationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Reservation, Lot, CustomUser
from django.contrib.auth import get_user
from datetime import date

@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'app/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/login.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required(login_url='/login/')
def dashboard(request):
    options = {
        'Reservation': {
            'url': reverse_lazy('app:reservation'),
            'title': 'Reserve a slot',
            'description': 'Reserve a slot for a loved one'},
        'Maps': {
            'url': reverse_lazy('app:map'),
            'title': 'View the map',
            'description': 'View the cemetery map and plot locations'},
        'Navigation': {
            'url': reverse_lazy('app:navigation'),
            'title': 'Navigate to the lots',
            'description': 'Get directions and navigate to the plots'}
    }
    block_numbers = Lot.objects.values('block_no').distinct()

    block_numbers_with_lots = []
    for block_number in block_numbers:
        lots = Lot.objects.filter(block_no=block_number['block_no'], capacity__gt=0)
        reserved_lots = Reservation.objects.filter(Lot__block_no=block_number['block_no'])
        block_numbers_with_lots.append({
            'block_number': block_number['block_no'],
            'lots': lots,
            'reserved_lots_count': reserved_lots.count(),
        })

   
    
    context = {'options': options,'block_numbers_with_lots': block_numbers_with_lots,}
    return render(request, 'app/dashboard.html', context)
def generate_transaction_number():
    today = date.today()
    last_reservation = Reservation.objects.filter(date_reserved=today).order_by('transaction_no').last()
    last_transaction_number = int(last_reservation.transaction_no[-2:]) if last_reservation else 0
    new_transaction_number = last_transaction_number + 1
    transaction_number = today.strftime('%m%d%y') + '-' + str(new_transaction_number).zfill(2)
    return transaction_number
@login_required(login_url='/login/')

def reservation(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():

            reservation = form.save(commit=False)
            reservation.user  = request.user
            reservation.save()
            return redirect('app:dashboard')  # Replace 'reservation_success' with the URL or view name for the reservation success page
    else:
        initial_data = {
            'date_reserved': date.today().strftime('%Y-%m-%d'),
            'transaction_no': generate_transaction_number(),
        }
        form = ReservationForm(initial=initial_data)
    return render(request, 'app/reservation.html', {'form': form,'data':generate_transaction_number()})


def map(request):
    from django.core import serializers
    import json
    lots = Lot.objects.all()
    lots_json = serializers.serialize('json',lots)        
    return render(request, 'app/mapa.html', {'lots_data':lots_json})

@login_required(login_url='/login/')
def navigation(request):
    return render(request, 'app/navigation.html')

    
