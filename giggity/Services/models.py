from django.db import models

class Service(models.Model):
    is_recurring = models.BooleanField()
    post = models.OneToOneField('Posts', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
