from django.http import HttpRequest, JsonResponse,  HttpResponseBadRequest
from faker import Faker
from .models import Student


fake = Faker()


def generate_student(request):
    student_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        'birth': fake.date_of_birth(minimum_age=18, maximum_age=30),
    }
    student = Student.objects.create(**student_data)
    return JsonResponse({'message': 'Student created successfully', 'student_id': student.id})


def generate_students(request):
    count = request.GET.get('count', 1)

    try:
        count = int(count)
    except ValueError:
        return HttpResponseBadRequest('write integer')
    if count <= 0 or count > 100:
        return HttpResponseBadRequest('Count should be a positive integer between 1 and 100')
    students = []

    for i in range(count):
        student_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            'birth': fake.date_of_birth(minimum_age=18, maximum_age=30),
        }
        student = Student.objects.create(**student_data)
        students.append({
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'birth': student.birth,
        })
    return JsonResponse({'students': students})