from django.contrib import admin

# Register your models here.
from .models import Matkul
from .models import Profesi
from .models import Matkur
from .models import Profesi_Matkul
from .models import Profesi_Matkur

class MatkulAdmin(admin.ModelAdmin):
    list_display = ('kdmk', 'matkul', 'semester')
admin.site.register(Matkul, MatkulAdmin);
admin.site.register(Profesi);
admin.site.register(Matkur);
admin.site.register(Profesi_Matkul);
admin.site.register(Profesi_Matkur);

