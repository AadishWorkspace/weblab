from django import forms
import datetime

EMPLOYEE_CHOICES = [
    ('EMP001', 'EMP001'),
    ('EMP002', 'EMP002'),
    ('EMP003', 'EMP003'),
]

class PromotionForm(forms.Form):
    employee_id = forms.ChoiceField(choices=EMPLOYEE_CHOICES)
    date_of_joining = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=datetime.date.today
    )
