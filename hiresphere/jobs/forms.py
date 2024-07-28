# jobs/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Company, Candidate

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CompanySignUpForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    website = forms.URLField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            company = Company.objects.create(
                user=user,
                name=self.cleaned_data['company_name'],
                description=self.cleaned_data['description'],
                website=self.cleaned_data['website']
            )
            company.save()
        return user
