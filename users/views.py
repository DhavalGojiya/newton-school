from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SchoolUserModelForm, SchoolUserLoginForm, FormChangePassword, SchoolUserEditForm
from .models import SchoolUser


# Create your views here.
def choose_user(request):
    return render(request, "users/user_choice.html")


def student_registration(request):
    """
    this is Student Registration form method. we are specifying users/registration/student
    URL for students only. SchoolUserModelForm have a Meta class where we re-used
    existing django models. that models automatically converted into input field forms.
    when any new registration hits this method it's Student registration hence we use
    reg.user_type = 'S'. it will add user type 'Student' in the database along with user.
    """
    if request.method == 'POST':
        student_reg_form = SchoolUserModelForm(request.POST, request.FILES)
        print("I AM REQUEST POST++ DATA++", request.POST)

        if student_reg_form.is_valid():
            reg = student_reg_form.save(commit=False)
            print("CLEANED DATA +++", student_reg_form.cleaned_data, end='\n\n')
            reg.user_type = 'S'
            reg.set_password(student_reg_form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return redirect('user_submit')

    else:
        student_reg_form = SchoolUserModelForm()
    return render(request, "users/student_register.html", {'form': student_reg_form})


def teacher_registration(request):
    """
    this is Teacher Registration form method. we are specifying users/registration/teacher
    URL for teachers only. SchoolUserModelForm have a Meta class where we re-used
    existing django models. that models automatically converted into input field forms.
    when any new registration hits this method it's Teacher registration hence we use
    reg.user_type = 'T'. it will add user type 'Teacher' in the database along with user.
    """
    if request.method == 'POST':
        teacher_reg_form = SchoolUserModelForm(request.POST, request.FILES)
        if teacher_reg_form.is_valid():
            reg = teacher_reg_form.save(commit=False)
            reg.user_type = 'T'
            reg.set_password(teacher_reg_form.cleaned_data.get('password'))
            # Final Save Data to database
            reg.save()
            return HttpResponseRedirect(reverse('user_submit'))

    else:
        teacher_reg_form = SchoolUserModelForm()
    return render(request, "users/teacher_register.html", {'form': teacher_reg_form})


def thanks_submission(request):
    """
    when any Student or Teacher Successfully registered their profile in our
    website, this method renders a Thank you for your registration HTML template.
    """
    return render(request, 'users/user_success_submit.html')


def users_login(request):
    """
    after succesfully registration for both of the user Student & Teacher, they
    need to Authenticate their self in our website. this method accepts POST
    request when user try to log in & Authenticate himself/herself in this website.
    this method using backend auth to verify user credentials. user must have to verify
    their credentials according to their previous registration credentials.
    """
    if request.method == 'POST':
        user_login_form = SchoolUserLoginForm(request.POST)
        if user_login_form.is_valid():
            user = user_login_form.cleaned_data
            if user:
                login(request, user)
                return redirect('school_dashboard')
        else:
            return render(request, 'users/users_login.html', {'form': user_login_form})
    else:
        if request.user.is_authenticated:
            print("Yes I Am Authenticated")
            # return render(request, 'users/user_already_login.html')
            # Send Him/Her Same Dashboard URL....
            return HttpResponseRedirect(reverse('school_dashboard'))

        else:
            user_login_form = SchoolUserLoginForm()
    return render(request, 'users/users_login.html', {'form': user_login_form})


# User Logout
def log_out(request):
    logout(request)
    return redirect('school_dashboard')


# User Password Reset
def user_change_pass(request):
    """
    this method is for changing user's password, keep in mind that here this
    form inherited Django built-in PasswordChangeForm. this form is not model form.
    it is built-in Django password change from which inherits SetPassword form.
    here SetPassword form directly inherits from (forms.Form).
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            user_pass_change_form = FormChangePassword(user=request.user, data=request.POST)
            if user_pass_change_form.is_valid():
                print("DICT++", user_pass_change_form.__dict__)
                user_pass_change_form.save()
                return HttpResponse("Successfully Changed your password")
        else:
            user_pass_change_form = FormChangePassword(user=request.user)
        return render(request, "users/change_password.html", {'form': user_pass_change_form})
    else:
        return HttpResponseRedirect(reverse('users_login'))


def users_dataset(request):
    context = {"dataset": SchoolUser.objects.all()}
    return render(request, "users/users_dataset.html", context)


def user_detail_data(request, ids):
    SchoolUser.objects.get(id=ids).delete()
    return HttpResponseRedirect(reverse('users_dataset'))


def user_profile_edit(request):
    """
    1 - user can change/update their account information.
    2 - this method verifies SchoolUserEditForm and generated cleaned_data.
    3 - SchoolUserEditForm carrying needful user fields.
    4 - this form inherit SchoolUserModelForm, which is a ModelForm.
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            user_edit_form = SchoolUserEditForm(request.POST, request.FILES, instance=request.user)
            if user_edit_form.is_valid():
                user_edit_form.save()
                messages.success(request, message='profile Updated successfully..')
                # return HttpResponseRedirect(reverse('school_dashboard'))
        else:
            user_edit_form = SchoolUserEditForm(instance=request.user)
    else:
        return HttpResponseRedirect(reverse('users_login'))
    return render(request, "users/user_profile_edit.html", {'user_edit_fm': user_edit_form})
