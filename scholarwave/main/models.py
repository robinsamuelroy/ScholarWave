from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Teacher(CustomUser):
    qualification  =   models.CharField(max_length=200)
    mobile_no      =   models.CharField(max_length=20)
    address        =   models.TextField()

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

class CourseCategory(models.Model):
    title        =   models.CharField(max_length=150)
    description  =   models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Course Category')
        verbose_name_plural = _('Course Categories')

class Course(models.Model):
    category    = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    teacher     = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses_taught')
    title       = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

class Student(CustomUser):
    qualification         =   models.CharField(max_length=200)
    mobile_no             =   models.CharField(max_length=20)
    address               =   models.TextField()
    interested_categories = models.TextField()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
            verbose_name = _('Student')
            verbose_name_plural = _('Students')

