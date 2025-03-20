from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def update_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        course.name = request.POST['name']
        course.save()
        return redirect('course_list')
    return render(request, 'course/update_course.html', {'course': course})

def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course_list')
