from django.contrib.auth.models import (AbstractBaseUser, Group, Permission,
                                        PermissionsMixin)
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Define or import the username_validator
username_validator = RegexValidator(
    regex=r'^[\w.@+-]+$',
    message=_('Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.')
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change related_name to avoid clash
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change related_name to avoid clash
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='customuser',
    )

    # Add other fields and methods as needed
    # ...

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
