from django import forms

from my_plant.plant.models import Profile, Plant



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'