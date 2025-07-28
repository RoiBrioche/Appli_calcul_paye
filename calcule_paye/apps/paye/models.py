from django.db import models


class MonthReport(models.Model):
    month = models.DateField()  # On utilisera le premier jour du mois comme repère
    hours_worked = models.DecimalField(max_digits=6, decimal_places=2)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    # Participation aux tickets resto (pris en charge par l'employeur ?)
    employer_ticket_contrib = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    # 💰 Données calculées ou entrées pour vérification
    actual_salary_received = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    actual_tickets_received = models.IntegerField(null=True, blank=True)
    actual_gratification_received = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    notes = models.TextField(blank=True)

    def estimated_salary(self):
        return self.hours_worked * self.hourly_rate

    def estimated_ticket_value(self):
        # Exemple : 1 ticket par jour travaillé
        return self.estimated_working_days() * self.employer_ticket_contrib

    def estimated_working_days(self):
        return round(float(self.hours_worked) / 7.0)  # si on considère 7h/jour

    def total_estimated(self):
        return self.estimated_salary() + self.estimated_ticket_value()

    def delta_salary(self):
        if self.actual_salary_received is not None:
            return self.actual_salary_received - self.estimated_salary()
        return None

    def delta_tickets(self):
        if self.actual_tickets_received is not None:
            return self.actual_tickets_received - self.estimated_working_days()
        return None
