from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

# Create your views here.

def pet_list(request):
	pets = Pet.objects.all()
	context = {
		"pets": pets,
	}
	return render(request, 'list.html', context)


def pet_detail(request, pet_id):
	pet = Pet.objects.get(id=pet_id)
	context = {
		"pet": pet,
	}
	return render(request, 'detail.html', context)


def pet_create(request):
	form = PetForm()
	if request.method == "POST":
		form = PetForm(request.POST , request.FILES)
		if form.is_valid():
			form.save()
			return redirect('pet-list')
	context = {
		"form": form,
	}
	return render(request, 'create.html' , context)


def pet_update(request, pet_id):
	pet_obj = Pet.objects.get(id=pet_id)
	form = PetForm(instance = pet_obj)
	if request.method == "POST":
		form = PetForm(request.POST , instance=pet_obj)
		if form.is_valid():
			form.save()
			return redirect('pet-list')
	context = {
        "pet_obj": pet_obj,
        "form": form,
    }
	return render(request, 'update.html', context)



def pet_delete(request, pet_id):
	pet_obj = Pet.objects.get(id=pet_id)
	pet_obj.delete()
	return redirect('pet-list')