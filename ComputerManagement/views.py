from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Computer
from .models import ComputerSystemSetting
from .models import ComputerNetworkSetting
from django.template import loader
from .forms import RegisterComputer


# Create your views here.
def index(request):
    computer_list = Computer.objects.order_by("computer_name")
    template = loader.get_template('index.html')
    context = {
        'computer_list': computer_list
    }
    return HttpResponse(template.render(context, request))

def register_computer(request):
    if request.method == 'POST':
        form = RegisterComputer(request.POST)
        if form.is_valid():
            return HttpResponse("New computer Name: " + form.cleaned_data["computer_name"])
    else:
        form = RegisterComputer()
        return render(request, 'register_computer.html', {'form': form})
