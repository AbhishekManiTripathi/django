from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm # django inbulit class which can be converted into html form
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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

@login_required # now this method will run only when user is logged (to prevent direct writing of end points)
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def profile(request):

    if request.method == 'POST':  # when we submit new data
        u_form =  UserUpdateForm( request.POST,  instance = request.user)  # user update form
        p_form =  ProfileUpdateForm( request.POST, request.FILES,   instance = request.user.profile) # profile update form

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else :
        u_form =  UserUpdateForm(instance = request.user)  # user update form
        p_form =  ProfileUpdateForm(instance = request.user.profile) # profile update form
        



    context = {

        'u_form' : u_form,
        'p_form' : p_form

    }

    return render(request, 'users/profile.html', context)

    




# messages.debug
# messages.warning
# messages.success
# messages.info
# messages.error