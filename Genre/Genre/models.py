from django.db import models


class Text(models.Model):
    Text = models.TextField()
    Genre = models.CharField(max_length=50)
    Report = models.TextField()

    def __str__(self):
        return f"Text{self.pk}"


