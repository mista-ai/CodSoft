from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
        ('OH', 'On Hold'),
        ('X', 'Canceled'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_priority_display()}, {self.get_status_display()})"
