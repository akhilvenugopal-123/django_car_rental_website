from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Rental
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    cars = Car.objects.all()
    print(cars)  
    return render(request, 'home.html', {'cars': cars})


@login_required(login_url='login')
def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    if request.method == 'POST':
        rental = Rental.objects.filter(car=car, returned=False).first()
        if rental:
            message = " Sorry this car is on a ride. Please choose another car."
        else:
            return_date = request.POST.get('return_date')
            if return_date:
                rental = Rental(user=request.user, car=car, return_date=return_date)
                rental.save()
                message = f"Booking successful! You've rented {car.name} until {return_date}."
            else:
                message = "Please choose a return date."
    else:
        message = ""
    
    return render(request, 'car_details.html', {'car': car, 'message': message})

def user_logout(request):
    logout(request)
    return redirect('login')

