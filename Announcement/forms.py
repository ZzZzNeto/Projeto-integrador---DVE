from django.forms import ModelForm
from django import forms
from .models import Annoucement, Tags 

class AnnouncementForm(ModelForm):
        CHOICES_COURSE = (
        ("ADS", "Ads"),
        ("APICULTURA", "Apicultura"),
        ("ALIMENTOS", "Alimentos"),
        )

        tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(),widget=forms.CheckboxSelectMultiple, required = False)
        curricular = forms.BooleanField(required = False)
        course = forms.ChoiceField(choices=CHOICES_COURSE, required=False)
        total_workload = forms.CharField(max_length=5, required=False)
 
        class Meta: 
                model = Annoucement
                fields = 'image_annoucement', 'requirements' ,'name_of_company', 'street', 'district', 'number','registration_deadline', 'tags', 'workload', 'vacancies', 'period', 'benefits', 'activities', 'email', 'phone','whatsapp', 'linkedin', 'instagram', 'description', 'curricular', 'course', 'total_workload'