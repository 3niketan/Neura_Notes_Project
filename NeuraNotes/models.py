from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    title = models.CharField(max_length=200)

    content = models.TextField()

    ai_title = models.CharField(max_length=200, blank=True, default='')
    ai_summary = models.TextField(blank=True, default='')
    ai_grammar = models.TextField(blank=True, default='')

    summary = models.TextField(blank=True, null=True)

    is_pinned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Note {self.pk}"
