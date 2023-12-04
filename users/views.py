from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm , ProfileUpdateForm , UserUpdateForm


def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Your Account has been created successfully! You can Login now')
            return redirect('login')          
    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html' , {"form":form , "title" :"Register"})
# Create your views here.


#decorator which is used to enhance the functionality of the function 
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your Account Info has been Updated successfully!')
            return redirect('profile')          
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
        "title":"Profile",
    }
    return render(request , "users/profile.html" , context)

'''
messages.debug()
messages.success()
messages.warning()
messages.error()
'''