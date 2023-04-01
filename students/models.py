from django.db import models


class CourseAddToCart(models.Model):
    teacher_course = models.ForeignKey('teachers.courses', on_delete=models.CASCADE)


class CoursePurchases(models.Model):
    course_add_cart = models.ForeignKey('CourseAddToCart', on_delete=models.CASCADE)
    enroll_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_courses_purchase'
