from django import forms
from .models import IdCredentials, IdType

class IdCredentialsForm(forms.ModelForm):
    class Meta:
        model = IdCredentials
        fields = ['owner', 'idCred_name', 'idCred_addr', 'idCred_dob']

        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'id_owner', 'type': 'hidden'})
        }

class IdTypeForm(forms.ModelForm):
    class Meta:
        model = IdType
        exclude = ['slug', 'owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        id_kind = self.data.get('idType_kind') or self.initial.get('idType_kind', None)

        if id_kind == 'passport':
            self.fields['idType_issauth'].required = True
            self.fields['idType_expdate'].required = False
        elif id_kind == 'license':
            self.fields['idType_expdate'].required = True
            self.fields['idType_issauth'].required = False
        else:
            self.fields['idType_issauth'].required = False
            self.fields['idType_expdate'].required = False
