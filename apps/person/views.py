from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.person.models import Person
from django.utils import timezone
from datetime import datetime

def index(request):
	print request.GET
	print request.method
	persons = Person.objects.all().order_by('zip_code')
	context = {
	'persons': persons,
	}
	return render(request, 'person/index.html', context)

def create(request):
	print "Creating a person"
	errors = []
	person = Person()
	person.first_name = request.POST.get('first_name')
	person.last_name = request.POST.get('last_name')
	person.zip_code = request.POST.get('zip')
	person.city = request.POST.get('city')
	if len(request.POST.get('first_name')) < 4:
		errors.append('First name must be at least 4 characters!')
	if len(request.POST.get('last_name')) < 4:
		errors.append('Last name must be at least 4 characters!')
	if len(request.POST.get('zip')) < 5:
		errors.append('Must enter a valid zip code!')
	if len(request.POST.get('city')) < 4:
		errors.append('City must be at least 4 characters!')
	if not errors:
		person.save()
		print "Success!"
		return redirect('/')
	else:
		return render(request, 'person/new.html', {'errors': errors})
	
def new(request):
	print "Going to create a new person"
	return render(request, 'person/new.html')

def delete(request, person_id):
	print "deleting person"
	person = Person.objects.get(id=person_id)
	person.delete()
	return redirect('/')

def edit(request, person_id):
	print "editing person"
	person = Person.objects.get(id=person_id)
	context = { 'person': person }
	return render(request, 'person/edit.html', context )

def update(request):
	print "updating person"
	update_errors = []
	person = Person.objects.get(id=request.POST.get('id'))
	person.first_name = request.POST.get('first_name')
	person.last_name = request.POST.get('last_name')
	person.city = request.POST.get('city')
	person.zip_code = request.POST.get('zip')
	if len(request.POST.get('first_name')) < 4:
		update_errors.append('First name must be at least 4 characters!')
	if len(request.POST.get('last_name')) < 4:
		update_errors.append('Last name must be at least 4 characters!')
	if len(request.POST.get('zip')) < 5:
		update_errors.append('Must enter a valid zip code!')
	if len(request.POST.get('city')) < 4:
		update_errors.append('City must be at least 4 characters!')
	if not update_errors:
		person.save()
		print "Success!"
		return redirect('/')
	else:
		context = { 'update_errors': update_errors, 'person': person }
		return render(request, 'person/edit.html', context)

def profile(request, person_id):
	print "viewing person"
	person = Person.objects.get(id=person_id)
	context = { 'person': person }
	return render(request, 'person/profile.html', context)