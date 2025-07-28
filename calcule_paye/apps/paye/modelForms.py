from django import forms
from .models import MonthReport

class MonthReportForm(forms.ModelForm):
    class Meta:
        model = MonthReport
        fields = [
            'month', 'hours_worked', 'hourly_rate',
            'employer_ticket_contrib',
            'actual_salary_received', 'actual_tickets_received',
            'actual_gratification_received', 'notes'
        ]
