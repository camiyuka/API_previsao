from django.db import models

# Create your models here.

class PrevisaoModel(models.Model):
    
    localizacao = models.CharField(max_length=100)
    data_previsao = models.DateField()
    temperatura = models.IntegerField()
    pressao_atmosferica = models.FloatField()
    umidade = models.FloatField()
    precipitacao = models.FloatField()
    condicao = models.CharField(max_length=100)

    def __str__(self):
        return f"Previsao(localizacao={self.localizacao}, data_previsao={self.data_previsao}, temperatura={self.temperatura}, pressao_atmosferica={self.pressao_atmosferica}, umidade={self.umidade}, precipitacao={self.precipitacao}, condicao={self.condicao})"
        "__all__"
    
    