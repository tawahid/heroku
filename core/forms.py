from django import forms
from core.models import MessagesModel

class MessagesForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message', 'rows':'5', 'class':'form-control form-control-sm'}
    ))
    class Meta:
        model = MessagesModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessagesForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not field == 'message':
                self.fields[field].widget.attrs = {'class': 'form-control form-control-sm'}
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label