from django.shortcuts import render, redirect
from .forms import TeacherCoursesModelForm
from django.http import HttpResponse
from users.models import USER_CHOICE_VALUE_STUDENT, USER_CHOICE_VALUE_TEACHER
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Courses
from django.http import JsonResponse
from django.views.generic import DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def teacher_courses(request):
    if request.user.is_authenticated:
        if request.user.user_type == USER_CHOICE_VALUE_TEACHER:
            course_form = TeacherCoursesModelForm()
            if request.method == "POST":
                course_form = TeacherCoursesModelForm(request.POST)
                if course_form.is_valid():
                    final_course_save = course_form.save(commit=False)
                    final_course_save.teacher = request.user
                    final_course_save.save()
                    return redirect('course_success')
            return render(request, 'teachers/teacher_courses_add.html', {'form': course_form})
        else:
            return HttpResponse("You Are Not Teacher..")
    else:
        return HttpResponseRedirect(reverse('users_login'))


def course_success_add(request):
    return render(request, 'teachers/course_added_success.html')


class CoursesManageView(LoginRequiredMixin, ListView):
    model = Courses
    template_name = 'teachers/manage_courses.html'
    context_object_name = 'course_data'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        elif not request.user.user_type == USER_CHOICE_VALUE_TEACHER:
            LOGIN_URL = self.get_login_url()
            return redirect(LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        return render(request, self.template_name, context)

    # Override get_queryset for filtering current login teacher courses
    def get_queryset(self):
        qs = super().get_queryset()
        current_login_teacher_courses = qs.filter(teacher=self.request.user)
        return current_login_teacher_courses

    # Override get_context_data to send some extra forms
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        instance = None
        context['form'] = TeacherCoursesModelForm(instance=instance)
        return context


class CoursesDeleteView(DeleteView):
    model = Courses

    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Get Request Forbidden </h1>")

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        data = {'success': True, 'message': 'Course Delete....'}
        return JsonResponse(data)

    # Only Courses Available with current user teacher
    def get_queryset(self):
        qs = super().get_queryset()
        current_login_teacher_courses = qs.filter(teacher=self.request.user)
        return current_login_teacher_courses


class CoursesUpdateView(UpdateView):
    model = Courses
    form_class = TeacherCoursesModelForm
    success_url = "/teachers/courses/manage"

    def get(self, request, *args, **kwargs):
        return JsonResponse({'method': "Get Method Not Allowed."})

    def form_valid(self, form):
        form.save()
        return JsonResponse({"status": "success", 'message': 'form updated successfully..'})

    def form_invalid(self, form):
        return JsonResponse({"status": "failed", 'errors': form.errors})
