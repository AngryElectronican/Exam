from django.db import models

class User_model(models.Model):
    """Model definition for Users."""
    id=models.IntegerField(primary_key=True)
    user=models.CharField(max_length=50)

    class Meta:
        db_table="User_model"

    def __str__(self):
        return self.user

# Create your models here.
