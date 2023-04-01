from django.shortcuts import render
from teachers.models import Courses
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import USER_CHOICE_VALUE_TEACHER, USER_CHOICE_VALUE_STUDENT


# Create your views here.
def newton_school_dashboard(request):
    return render(request, "newtonschool/dashboard.html", )


def newton_school_about(request):
    return render(request, "newtonschool/about.html")


class CoursesListView(ListView):
    model = Courses
    template_name = 'newtonschool/courses.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == USER_CHOICE_VALUE_TEACHER:
            self.object_list = super().get_queryset()
            context = super().get_context_data(**kwargs)
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect(reverse('school_dashboard'))
