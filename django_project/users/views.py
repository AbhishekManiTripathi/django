from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm # django inbulit class which can be converted into html form
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 

# UserCreationForm has been replaced by UserRegisterForm
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
            
    else :
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form} ) 

@login_required # now this method will run only when user is logged (to prevet direct writing of end points)
def profile(request):
    return render(request, 'users/profile.html')    



# messages.debug
# messages.warning
# messages.success
# messages.info
# messages.error