from django.shortcuts import render,redirect
from clinicalsApp.models import Patient, ClinicData
from clinicalsApp.forms import PatientForm, ClinicDataForm

# Create your views here.
def index(request):
    return render(request,'clinicalsApp/index.html',{})

def getPatients(request):
    patients = Patient.objects.all()
    return render(request,'clinicalsApp/allPatients.html',{'patients':patients})

def getPatient(request,id):
    patient = Patient.objects.get(id=id)
    return render(request,'clinicalsApp/patientProfile.html',{'patient':patient})

def addPatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/addPatient.html',{'form':form})

def updatePatient(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
        return redirect('/patientProfile/{}'.format(patient.id))
    return render(request,'clinicalsApp/updatePatient.html',{'form':form})

def deletePatient(request,id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('/allPatients')

def addMedicalData(request):
    form = ClinicDataForm()
    if request.method == 'POST':
        form = ClinicDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/allRecords')
    return render(request,'clinicalsApp/addClinicData.html',{'form':form})

def allClinicData(request):
    all_clinic_data = ClinicData.objects.all()
    return render(request,'clinicalsApp/allClinicData.html',{'all_clinic_data':all_clinic_data})
