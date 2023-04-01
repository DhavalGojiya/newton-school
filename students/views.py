from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from teachers.models import Courses
from .forms import StudentEnrollCourseModelForm
from school import settings
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404


# Create your views here.


class StudentCoursesEnrollDetailView(DetailView):
    # NEED IMPROVEMENTS ---->
    template_name = 'students/student_enroll_courses.html'
    model = Courses

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Courses, pk=self.kwargs['pk'])


class StudentCourseBillingView(TemplateView):
    template_name = 'students/student_enroll_courses_billing.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentEnrollCourseModelForm()
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        student_enroll = StudentEnrollCourseModelForm(request.POST)
        if student_enroll.is_valid():
            stu_enroll_model_object = student_enroll.save(commit=False)
            stu_enroll_model_object.student_standard = request.user.standard
            stu_enroll_model_object.price = 0
            # Final Database Save
            stu_enroll_model_object.save()

            return HttpResponseRedirect(reverse('school_dashboard'))
        else:
            return render(request, self.template_name, {'form': student_enroll})
