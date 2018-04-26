from django.shortcuts import render
from .models import Check
# Create your views here.


def show_check(request):
	name = Check.objects.all()
	# context['name'] = Check.objects.all()
	return render(request, 'my_app/show.html', {'name': name})