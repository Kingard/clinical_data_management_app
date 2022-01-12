from django import forms
from clinicalsApp.models import Patient, ClinicData

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicDataForm(forms.ModelForm):
    class Meta:
        model = ClinicData
        fields = '__all__'
