from django.shortcuts import render
from django.views import View
from cekprofesi.models import Matkul
from cekprofesi.models import Matkur
from cekprofesi.models import Profesi
from cekprofesi.models import Profesi_Matkul
from cekprofesi.models import Profesi_Matkur

def index(request):
    semester1 = Matkul.objects.filter(semester=1)
    semester2 = Matkul.objects.filter(semester=2)
    semester3 = Matkul.objects.filter(semester=3)
    semester4 = Matkul.objects.filter(semester=4)
    semester5 = Matkul.objects.filter(semester=5)
    semester6 = Matkul.objects.filter(semester=6)
    semester7 = Matkul.objects.filter(semester=7)
    semester8 = Matkul.objects.filter(semester=8)
    kursus1 = Matkur.objects.filter(semester=1)
    kursus2 = Matkur.objects.filter(semester=2)
    kursus3 = Matkur.objects.filter(semester=3)
    kursus4 = Matkur.objects.filter(semester=4)
    kursus5 = Matkur.objects.filter(semester=5)
    kursus6 = Matkur.objects.filter(semester=6)
    context = {
        'Semesters1': semester1,
        'Semesters2': semester2,
        'Semesters3': semester3,
        'Semesters4': semester4,
        'Semesters5': semester5,
        'Semesters6': semester6,
        'Semesters7': semester7,
        'Semesters8': semester8,
        'Kursusz1': kursus1,
        'Kursusz2': kursus2,
        'Kursusz3': kursus3,
        'Kursusz4': kursus4,
        'Kursusz5': kursus5,
        'Kursusz6': kursus6,
    }
    return render(request,'index.html',context)
    #tempalte variabel bisa memasukan parameter
    