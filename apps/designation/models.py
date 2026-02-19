from django.db import models

# Create your models here.
import uuid
from django.db import models


class AbleDesignation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    company_id = models.UUIDField()

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "able_designations"
        unique_together = ('company_id', 'name')

    def __str__(self):
        return self.name
