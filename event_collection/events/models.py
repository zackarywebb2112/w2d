from django.db import models
from django.utils import timezone

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    
class Event(models.Model):
    unique_id = models.CharField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="events")
    ticket_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    catergory = models.CharField(max_length=100, blank=True, null=True)
    sub_catergory = models.CharField(max_length=100, blank=True, null=True)
    source_api = models.CharField(max_length=50)
    source_event_id = models.CharField(max_length=250, blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    is_user_submitted = models.BooleanField(default=False)
    is_promoted = models.BooleanField(default=False)
    approval_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'),('approved', 'Approved'),('rejected', 'Rejected')],
        default='approved'
    )
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('source_api', 'source_event_id')

    def __str__(self):
        return f"{self.title} at {self.venue.name} on {self.start_datetime.strftime('%Y-%m-%d')}"