from django import forms
from .models import Usuario, Carrera
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'carrera']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label="Contraseña Antigua", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('La contraseña antigua no es correcta.')
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError('Las nuevas contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

from django import forms
from .models import Prestamo

class SolicitarPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_devolucion']  # Suponiendo que sólo necesitas la fecha de devolución
        widgets = {
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'})
        }
