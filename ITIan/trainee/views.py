from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trainee
from .serializers import TraineeSerializer


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

#update API>>>>>>
@api_view(['PUT', 'PATCH'])
def update_trainee(request, pk):
    try:
        trainee = Trainee.objects.get(pk=pk)
    except Trainee.DoesNotExist:
        return Response({"error": "Trainee not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TraineeSerializer(trainee, data=request.data, partial=True)  # Allow partial updates

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def delete_trainee(request, id):
    trainee = Trainee.objects.get(id=id)
    trainee.delete()
    return redirect('trainee_list')


#>>>>>>>>>>>>>>>>>VIEWS>>>>>>>>>>>>>>>


# Create API Views Using Class-Based Views
class TraineeListView(generics.ListCreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer


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


class TraineeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer