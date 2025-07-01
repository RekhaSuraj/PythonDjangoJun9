from django.shortcuts import render,redirect
from appone.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from appone.forms import ClinicalDataForm
# Create your views here.
class patientListView(ListView):
    model = Patient
    # By default template name is patient_list.html
    # By default context name is patien
class PatientCrateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('Firstname','Lastname','Age')
     # By default template name is patient_form.html
    # By default context name is patient
class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('Firstname','Lastname','Age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')


def adddata(request, **kwargs):
    patient = Patient.objects.get(id=kwargs['pk'])
    form = ClinicalDataForm()

    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            clinical_data = form.save(commit=False)
            clinical_data.Patient = patient
            clinical_data.save()
            return redirect('/')  # or a proper URL name

    return render(request, 'appone/clinicaldata_form.html', {'form': form, 'patient': patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(Patient_id=kwargs['pk'])
    responseData = []

    for entry in data:
        responseData.append(entry)

        if entry.componentName == 'HW':
            # Expected value: "170/70" (Height in cm / Weight in kg)
            try:
                height, weight = entry.componentValue.split('/')
                height_in_meters = float(height) / 100
                bmi = float(weight) / (height_in_meters ** 2)

                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = f"{bmi:.2f}"
                responseData.append(bmiEntry)
            except Exception as e:
                print(f"Error calculating BMI: {e}")

    return render(request, 'appone/generateReport.html', {'data': responseData})

