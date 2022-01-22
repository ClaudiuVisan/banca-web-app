from django.forms import ModelForm
from Banca.models import Banci, Sucursale, Angajati


class BancaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BancaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Banci
        fields = '__all__'


class SucursalaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SucursalaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Sucursale
        fields = '__all__'


class AngajatForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AngajatForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Angajati
        fields = '__all__'


class BancaDeleteForm(ModelForm):
    class Meta:
        model = Banci
        fields = []


class SucursalaDeleteForm(ModelForm):
    class Meta:
        model = Sucursale
        fields = []


class AngajatDeleteForm(ModelForm):
    class Meta:
        model = Angajati
        fields = []