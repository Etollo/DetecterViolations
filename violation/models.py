from django.db import models


class Violation(models.Model):
    image = models.ImageField(null=False, default=None)
    time = models.DateTimeField()
    PLACE = (
        (1, 'Склад'),
        (2, 'Цех'),
    )
    place = models.CharField(max_length=100, choices=PLACE)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=1000, null=True, blank=True, default="Violation")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
