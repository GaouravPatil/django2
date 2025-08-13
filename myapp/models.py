from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-created_at']
