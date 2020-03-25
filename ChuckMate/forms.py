from django import forms

class UserForm(forms.Form):
    fname = forms.CharField(max_length=15,widget=forms.TextInput(
            attrs={
                'placeholder': 'Chuck'
            }
        ))
    #lname = forms.CharField(max_length=15,initial="Norris")
    lname = forms.CharField(max_length=15,widget=forms.TextInput(
            attrs={
                'placeholder': 'Norris'
            }
        ))
    re = forms.BooleanField(required=False)
