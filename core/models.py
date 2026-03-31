from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({'Teacher' if self.is_teacher else 'Student' if self.is_student else 'Admin'})"

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} - {self.section}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
    
    def __str__(self):
        return f"{self.name} ({self.classroom.name})"

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='teacher_profile')
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    designation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student_profile')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')
    roll_no = models.CharField(max_length=20, unique=True)
    admission_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} (Roll: {self.roll_no})"

class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])
    recorded_by = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"

class Fee(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.student.user.username} - {self.amount} ({'Paid' if self.is_paid else 'Pending'})"

class Result(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField(default=100.0)
    exam_date = models.DateField(default=timezone.now)
    remarks = models.TextField(blank=True, null=True)
    recorded_by = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.name}: {self.marks_obtained}/{self.total_marks}"
