from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})




def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add_trainee.html', {'form': form})

def update_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    if request.method == "POST":
        trainee.name = request.POST['name']
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})

def delete_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    trainee.delete()
    return redirect('trainee_list')
