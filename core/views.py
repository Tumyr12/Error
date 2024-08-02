from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "core/index.html")
    
def sign_up(request):
    return render(request, "core/sign_up.html")

def numbers(request):
    if request.method == 'POST':
        user_number = int(request.POST['user_guess'])
        random_number = random.randint(0,1)
        if random_number == user_number:
            result = 'Congrats sir'
        else:
            result = f'You lost sir the number was: {random_number}'
        return render(request, "core/numbers.html", {'result': result})
    return render(request, "core/numbers.html")