from django import forms

class RegistroFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    clave = forms.CharField()
    documento = forms.IntegerField()

class SociosFormulario(forms.Form):
    nro_socio = forms.IntegerField()
    clave = forms.CharField()

class EntradasFormulario(forms.Form):
    partido = forms.CharField()
    ubicacion = forms.CharField()
    valor = forms.DecimalField()



