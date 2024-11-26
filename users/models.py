from django.contrib.auth.models import AbstractUser
from django.db import models

# Role model to define different roles and permissions
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.JSONField(default=list)  # List of permissions

    def __str__(self):
        return self.name


# Custom User Model with role assignment
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='users',  # Add this related_name to avoid the conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='users',  # Add this related_name as well
        blank=True
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username