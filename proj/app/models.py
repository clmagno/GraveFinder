from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.utils.crypto import get_random_string
import hashlib
# Create your models here.


class CustomUserManager(BaseUserManager):
    def hash_password(password, salt):
        # Concatenate the password and salt
        password_with_salt = password + salt

        # Hash the concatenated string using a hashing algorithm (e.g., SHA256)
        hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()

        return hashed_password
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not user.salt:
            user.salt = get_random_string(32)

        hashed_password = hash_password(password, user.salt)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True,  default='')
    first_name = models.CharField(max_length=30,  default='')
    last_name =  models.CharField(max_length=30,  default='')
    email = models.EmailField(max_length=255, unique=True,  default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    salt = models.CharField(max_length=255, default='')
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    def save(self, *args, **kwargs):
        if not self.salt:
            # Generate a salt value if it is not already set
            self.salt = get_random_string(32)

        super().save(*args, **kwargs)   
class Lot(models.Model):
    id = models.AutoField(primary_key=True)
    block_no = models.CharField(max_length=50, default='')
    lot_no = models.CharField(max_length=50, default='')
    phase = models.CharField(max_length=50, default='')
    area = models.CharField(max_length=50, default='')
    capacity = models.PositiveIntegerField()
    lat_long1 = gis_models.PointField()
    lat_long2 = gis_models.PointField()
    lat_long3 = gis_models.PointField()
    lat_long4 = gis_models.PointField()
    
    def __str__(self):
        # Define a string representation for the model
        return f"Slot {self.id}"

class Corpse(models.Model):
    id = models.AutoField(primary_key=True)
    last_name= models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    slot = models.ForeignKey(Lot, on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.id
    
class Reservation(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    TRANSACTION_NUMBER_FORMAT = "%m%d%y-%m"

    transaction_no = models.CharField(max_length=100, primary_key=True, unique=True, editable=False)
    corpse_last_name = models.CharField(max_length=100, default='')
    corpse_first_name = models.CharField(max_length=100, default='')
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    Lot= models.ForeignKey(Lot, on_delete=models.CASCADE,  null=True)
    date_reserved = models.DateField(default=timezone.now)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        current_date = timezone.now().date()
        last_reservation = Reservation.objects.filter(date_reserved=current_date).order_by('transaction_no').last()
        last_transaction_number = int(last_reservation.transaction_no[-2:]) if last_reservation else 0
        new_transaction_number = last_transaction_number + 1
        formatted_date = current_date
        self.transaction_no = f"{formatted_date}-{new_transaction_number:02d}"

        super().save(*args, **kwargs)
    def __str__(self):
        return self.transaction_no