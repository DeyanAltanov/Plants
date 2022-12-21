from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

# Create your views here.
from my_plant.plant.forms import ProfileForm, PlantForm, DeletePlantForm, DeleteProfileForm
from my_plant.plant.models import Profile, Plant


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context=context)


def catalogue(request):
    profile = get_profile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'catalogue.html', context=context)


def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm()
    context = {
        'form': form,
    }
    return render(request, 'create-plant.html', context=context)


def plant_details(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {
        'plant': plant,
    }
    return render(request, 'plant-details.html', context=context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm(instance=plant)
    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'edit-plant.html', context=context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    else:
        form = DeletePlantForm(instance=plant)
    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context=context)


def profile_details(request):
    profile = get_profile()
    plants = Plant.objects.all()
    all_plants = plants.count()
    context = {
        'profile': profile,
        'plants': plants,
        'all_plants': all_plants,
    }
    return render(request, 'profile-details.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Plant.objects.all().delete()
        return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'game': profile,
    }
    return render(request, 'delete-profile.html', context=context)