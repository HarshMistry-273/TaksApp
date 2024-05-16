import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

priority_choices = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
status_choices = [('open','Open'), ('in_progress','In Progress'),('done','Done'),('canceled','Canceled')]

class Task(models.Model):
    """
    Task model to store task details.
    """
    tid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, default= "Untitled Task")
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(choices=priority_choices, max_length=20)
    status = models.CharField(choices=status_choices, max_length=20)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    
