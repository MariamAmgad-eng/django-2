from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required

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


#>>>>>>>>>>>>>>>>>VIEWS>>>>>>>>>>>>>>>

class TraineeListView(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'  # Create this template
    context_object_name = 'trainees'

class TraineeCreateView(LoginRequiredMixin, CreateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/trainee_form.html'  # Create this template
    success_url = reverse_lazy('trainee_list')

class TraineeUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainee
    form_class = TraineeForm
    template_name = 'trainee/trainee_form.html'
    success_url = reverse_lazy('trainee_list')

class TraineeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainee
    template_name = 'trainee/trainee_confirm_delete.html'
    success_url = reverse_lazy('trainee_list')


