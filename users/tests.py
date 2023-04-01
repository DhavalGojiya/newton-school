from django.test import TestCase
from django.shortcuts import reverse
from users.models import SchoolUser


class UserModelTest(TestCase):
    def setUp(self):
        """
        This is User Model Creation function which is then run by
        def test_user_creation function when developer runs Test cases.
        """
        data = {
            'username': 'admin',
            'first_name': 'Admin',
            'last_name': 'Sir',
            'password': 'Admin@123',
            'email': 'Admin10@gmail.com',
            'local_address': 'Florida'
        }
        self.user = SchoolUser.objects.create(**data)
        raw_password = data.get('password')
        self.user.set_password(raw_password)
        self.user.save()

    def test_user_creation(self):
        print("I AM 1st TEST CASE")
        """
        This test case will use to check the User creation verification status. It catches any errors occurred
        during creation process of User instance.
        """
        self.assertTrue(isinstance(self.user, SchoolUser))
        self.assertEqual(self.user.first_name, 'Admin')

    def test_user_student_register_url(self):
        """
        This test case will use to check the Student registration. It catches any errors occurred
        during student registration process.
        """
        print("I AM 2nd TEST CASE")
        student_data = {
            'first_name': 'Ajay',
            'last_name': 'Patel',
            'username': 'ajay10',
            'email': 'ajay10@gmail.com',
            'local_address': 'Mahesana',
            'standard': 11,
            'terms_conditions': True
        }
        url = reverse("student_reg")
        returnValue = self.client.post(url, data=student_data)

    def test_user_teacher_register_url(self):
        """
        This test case will use to check the Teacher registration. It catches any errors occurred
        during teacher registration process.
        """
        print("I AM 3rd TEST CASE")
        teacher_data = {
            'first_name': 'Alakh',
            'last_name': 'Pandey',
            'username': 'alakh10',
            'email': 'alakh10@gmail.com',
            'local_address': 'banglore',
            'subject': 'Physics',
            'terms_conditions': True
        }
        url = reverse("teacher_reg")
        returnValue = self.client.post(url, data=teacher_data)
