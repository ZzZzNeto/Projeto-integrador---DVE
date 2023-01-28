from django.forms import ModelForm
from django import forms
from .models import Annoucement, Tags 
from django.utils import timezone

class AnnouncementForm(ModelForm):

        registration_time = forms.DateField()
        tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple, required = False)
        curricular = forms.BooleanField(required = False)
        total_workload = forms.CharField(max_length=5, required=False)
        description = forms.CharField(max_length=500, required=False)

        def __init__(self, *args, **kwargs):
                super(AnnouncementForm, self).__init__(*args, **kwargs)
                self.fields['course'].required = False
        
        def clean_registration_time(self):
                data = self.cleaned_data['registration_time']
                if data < timezone.now().date():
                        raise forms.ValidationError("Prazo não pode ser anterior ao dia de hoje")
                return data
 
        class Meta: 
                model = Annoucement
                fields = 'image_annoucement', 'requirements' ,'name_of_company', 'street', 'district', 'number','registration_time', 'tags', 'workload', 'vacancies', 'period', 'benefits', 'activities', 'email', 'phone','whatsapp', 'linkedin', 'instagram', 'description', 'curricular', 'course', 'total_workload'

class FilterForm(forms.Form):
        tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple)

        def __init__(self ,*args, **kwargs):
                super(FilterForm, self).__init__(*args, **kwargs)