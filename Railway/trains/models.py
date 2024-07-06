from django.db import models
from django.contrib.auth.models import AbstractUser

class Trains(models.Model):
    categories = (
        ('Normal', 'Normal'),
        ('Express', 'Express')
    )
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    seats_total = models.IntegerField()
    seats_res = models.IntegerField()
    types = models.CharField(choices=categories, max_length=20)
    cost = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.id)


class Users(AbstractUser):
    username = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField(null=True)
    first_name = models.CharField(null=True, max_length=20)
    last_name = models.CharField(null=True, max_length=20)
    balance = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    num_booked = models.IntegerField()
    users = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    trains = models.ForeignKey(Trains, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
