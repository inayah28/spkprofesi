from django.db import models

class Matkul(models.Model):
    kdmk = models.CharField(max_length=9, primary_key=True, unique=True)
    matkul = models.CharField(max_length=9)
    semester = models.CharField(max_length=1)
    def __str__(self):
        return "{}".format(self.kdmk)

class ProfesiMatkul(models.Model):
    profesi = models.CharField(max_length=25, default="")
    kdmk = models.ForeignKey(Matkul,to_field="kdmk", db_column="kdmk")
    presentase = models.CharField(max_length=4) # --> harusnya 4 kalo formatnya 100%

    def __str__(self):
        return "{}.{}".format(self.id,self.profesi)

class Profesi(models.Model):
    kdprofesi = models.CharField(max_length=9, primary_key=True)
    profesi = models.CharField(max_length=50)
    unitk = models.TextField()
    def __str__(self):
        return "{}".format(self.profesi)

