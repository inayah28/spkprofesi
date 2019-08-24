from django.shortcuts import render
from django.http import HttpResponse
from .models import Matkul
from .models import Matkur
from .models import Profesi
from .models import Profesi_Matkul
from .models import Profesi_Matkur
import csv
from .modNormalize import normalize
from collections import Counter
from django.http import Http404
def index(request):
    profesi = Profesi.objects.all()
    context = {
        'Profesis':profesi,
        'judul':'TEKNIK INFORMATIKA',
    }
    if request.method == 'POST':
        nama_profesi = request.POST['name_profesi']
        matakuliah=Matkul.objects.filter(profesi_matkul__profesi=nama_profesi)
        profesi_matkur = Profesi_Matkur.objects.filter(profesi=nama_profesi)
        context = {
            'baru' :matakuliah,
            'Profesi_Matkurs' :profesi_matkur,
            'profesi':nama_profesi,
        }
        # return render(request,'sistem/profesi.html', context)
        if not matakuliah:          
            data_profesi = {
                'ADVANCE ANIMATOR':'cekprofesi/data/profesi/uk_aa.csv',
                'ADVANCE MOBILE COMPUTING':'cekprofesi/data/profesi/uk_amc.csv',
                'ADVANCE MULTIMEDIA DESIGNER':'cekprofesi/data/profesi/uk_amd.csv',
                'AUDITOR MADYA TEKNOLOGI INFORMASI':'cekprofesi/data/profesi/uk_amti.csv',
                'CLOUD COMPUTING DEVELOPER':'cekprofesi/data/profesi/uk_ccd.csv',
                'CYBER SECURITY ANALYST':'cekprofesi/data/profesi/uk_csa.csv',
                'DIGITAL ENTERPRENEUR DEPUTY MANAGER':'cekprofesi/data/profesi/uk_dedm.csv',
                'DEPUTY MANAGER ICT PROJECT MANAGEMENT':'cekprofesi/data/profesi/uk_dmipm.csv',
                'DATABASE PROGRAMMER':'cekprofesi/data/profesi/uk_dp.csv',
                'ENTERPRISE ARCHITECT':'cekprofesi/data/profesi/uk_ea.csv',
                'ERP ANALYST':'cekprofesi/data/profesi/uk_erpa.csv',
                'IT AUDITOR':'cekprofesi/data/profesi/uk_ia.csv',
                'ICTPM DEPUTY MANAGER':'cekprofesi/data/profesi/uk_idm.csv',
                'INTERMEDIATE GRAPHIC DESIGNER ':'cekprofesi/data/profesi/uk_igd.csv',
                'LEAD PROGRAMMER':'cekprofesi/data/profesi/uk_lp.csv',
                'NETWORK ADMINISTRATOR':'cekprofesi/data/profesi/uk_na.csv',
                'NETWORK DESIGNER':'cekprofesi/data/profesi/uk_nde.csv',
                'NETWORK ADMINISTRATOR MADYA':'cekprofesi/data/profesi/uk_ndm.csv',
                'OBJECT PROGRAMMER':'cekprofesi/data/profesi/uk_op.csv',
                'PROGRAM ANALYST': 'cekprofesi/data/profesi/uk_pa.csv',
                'TEKNISI MADYA JARINGAN KOMPUTER':'cekprofesi/data/profesi/uk_tmjk.csv',
                'SENIOR COMPUTER TECHNICIAN SPECIALIST':'cekprofesi/data/profesi/uk_scts.csv',
                'SYSTEM ADMINISTRATOR':'cekprofesi/data/profesi/uk_sa.csv',
                'SYSTEM ANALYST':'cekprofesi/data/profesi/uk_san.csv',
                'TEKNISI PUSAT DATA MADYA':'cekprofesi/data/profesi/uk_tpdm.csv',
                'VIDEO EDITOR':'cekprofesi/data/profesi/uk_ve.csv',
                'WEB DEVELOPER':'cekprofesi/data/profesi/uk_wd.csv'          
            }
            data_rps = {
                'cekprofesi/data/matkul/sap_ap1.csv':('IT045201','ALGORITMA PEMROGRAMAN 1'),
                'cekprofesi/data/matkul/sap_ap2.csv':('IT045202','ALGORITMA PEMROGRAMAN 2'),
                'cekprofesi/data/matkul/sap_ap3.csv':('IT045203','ALGORITMA PEMROGRAMAN 3'),
                'cekprofesi/data/matkul/sap_gk1.csv':('AK045205','GRAFIK KOMPUTER 1'),
                'cekprofesi/data/matkul/sap_gk2.csv':('AK045206','GRAFIK KOMPUTER 2'),
                'cekprofesi/data/matkul/sap_pbo.csv':('AK045213','PEMROGRAMAN BERBASIS OBJECT'),
                'cekprofesi/data/matkul/sap_skk.csv':('IT045237','SISTEM KEAMANAN KOMPUTER'),
                'cekprofesi/data/matkul/sap_rpl2.csv': ('AK04522','REKAYASA PERANGKAT LUNAK')
            }

            for profesi1, dataset_profesi in data_profesi.items():
                if request.POST.get('name_profesi') == profesi1:
                    with open (dataset_profesi, 'r', encoding = 'utf-8')as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)
                        list_kw_profesi = []
                        for row in csv_file:
                            usenorm = normalize()
                            text_norm = usenorm.tokenize(row)
                            list_kw_profesi.extend(text_norm)
                        keyword_profesi = Counter(list_kw_profesi)

            profesi_matkul = []
            for dataset_rps, matkul1 in data_rps.items():
                with open(dataset_rps, 'r', encoding = "utf-8") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)
                    list_kw_rps = []
                    for row in csv_file:
                        usenorm = normalize()
                        text_norm = usenorm.tokenize(row)
                        list_kw_rps.extend(text_norm)
                    keyword_rps = Counter(list_kw_rps)

                    def jaccard_similarity(x, y):
                        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
                        union_cardinality = len(set.union(*[set(x), set(y)]))
                        return intersection_cardinality/float(union_cardinality)

                    hasil = jaccard_similarity(list_kw_profesi, list_kw_rps)
                    hasil_percen = '{0:.0%}'.format(hasil)
                    kata_sama = set.intersection(*[set(list_kw_profesi), set(list_kw_rps)])

                    print ('Hasil Similarity Profesi '+request.POST.get('name_profesi')+ ' dan matkul ' +matkul1[1]+ ' adalah ...')
                    print ('  ' +hasil_percen+ '\n')

                if hasil > 0:
                    profesi_matkul.append(matkul1)
                    print('daftar kata penting untuk profesi '+request.POST.get('name_profesi') + '\n')
                    print(str (list_kw_profesi)+ '\n\n')
                    print('daftar kata penting mata kuliah '+matkul1[1]+ '\n')
                    print(str(list_kw_rps)+ '\n\n')
                    print('jumlah masing masing kata penting profesi ' +request.POST.get('name_profesi')+ '\n')
                    print(str(len(keyword_profesi))+ '\n\n')
                    print('jumlah masing masing kata di sap matakuliah ' +matkul1[1]+'\n')
                    print(str(len(keyword_rps))+ '\n\n')
                    print('Hasil Similarity Profesi ' + request.POST.get('name_profesi') + ' dan sap matakuliah ' +matkul1[1]+ ' adalah \n')
                    print('('+str(len(kata_sama))+' / ('+str(len(keyword_rps))+' + '+str(len(keyword_profesi))+' - '+str(len(kata_sama))+'))* 100% = '+hasil_percen+ '\n\n')
                    print('kode unit yang sama di profesi '+request.POST.get('name_profesi')+ ' dan sap matkul ' +matkul1[1]+ ': \n')
                    print(str(kata_sama)+ '\n\n')
                    print('###\n\n')

            #insert matkul ke tabel Profesi_Matkul       
            for i in profesi_matkul:
                insert_table = Profesi_Matkul(profesi=request.POST.get('name_profesi'),kdmk=Matkul.objects.filter(kdmk=i).first(), presentase=hasil_percen)
                insert_table.save()

            matakuliah=Matkul.objects.filter(profesi_matkul__profesi=nama_profesi)
            profesi = Profesi.objects.filter(profesi=nama_profesi)
            context = {
               'baru' :matakuliah,
               'profesi':nama_profesi,
               'Profesis': profesi,
            }
                
            return render(request, 'sistem/index.html', context)
        
        else:
            matakuliah=Matkul.objects.filter(profesi_matkul__profesi=nama_profesi)
            
            profesi = Profesi.objects.filter(profesi=nama_profesi)
            context = {
                'baru' :matakuliah,
                'profesi':nama_profesi,
                'Profesis': profesi,
            }
            return render(request, 'sistem/index.html', context)

    return render(request, 'sistem/index.html', context)

