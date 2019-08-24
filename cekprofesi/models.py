from django.db import models

class Matkul(models.Model):
    kdmk = models.CharField(max_length=9, primary_key=True)
    matkul = models.CharField(max_length=9)
    semester = models.CharField(max_length=1)
    def __str__(self):
        return "{}".format(self.kdmk)

class Profesi_Matkul(models.Model):
    profesi = models.CharField(max_length=50, primary_key=True)
    kdmk = models.ForeignKey(Matkul, blank=True)
    presentase = models.CharField(max_length=4) # --> harusnya 4 kalo formatnya 100%

    def __str__(self):
        return "{}".format( self.profesi)

class Profesi(models.Model):
    kdprofesi = models.CharField(max_length=9, primary_key=True)
    profesi = models.CharField(max_length=50)
    unitk = models.TextField()
    def __str__(self):
        return "{}".format(self.profesi)

