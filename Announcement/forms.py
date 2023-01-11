from django.forms import ModelForm
from django import forms
from .models import Annoucement, Tags 

class AnnouncementForm(ModelForm):
        tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple, required = False)

        class Meta:
                model = Annoucement
                fields = 'image_annoucement', 'requirements' ,'name_of_company', 'street', 'district', 'number','registration_deadline', 'tags', 'workload', 'vacancies', 'period', 'benefits', 'activities', 'email', 'phone','whatsapp', 'linkedin', 'instagram', 'description'

        def save(self, commit=True):
                announce = super().save(commit=False)
                announce.save()
                announce.tags.set(self.cleaned_data['tags'])
                announce.creator.annoucement_set.add(announce)
                return announce