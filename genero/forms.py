from django import forms


class GeneroForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].error_messages = {'required': 'campo obrigatório'}

    descricao = forms.CharField(label='Gênero', required=True)
