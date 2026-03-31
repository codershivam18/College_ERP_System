from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentProfile, TeacherProfile, Classroom

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
    
    # Extra fields for profile
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    
    # Student specific fields
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), required=False)
    roll_no = forms.CharField(max_length=20, required=False)
    
    # Teacher specific fields
    designation = forms.CharField(max_length=100, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'phone', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        
        if commit:
            user.save()
            if role == 'student':
                StudentProfile.objects.create(
                    user=user,
                    classroom=self.cleaned_data.get('classroom'),
                    roll_no=self.cleaned_data.get('roll_no')
                )
            elif role == 'teacher':
                TeacherProfile.objects.create(
                    user=user,
                    designation=self.cleaned_data.get('designation')
                )
        return user

class AttendanceForm(forms.ModelForm):
    class Meta:
        from .models import Attendance
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ResultForm(forms.ModelForm):
    class Meta:
        from .models import Result
        model = Result
        fields = ['student', 'subject', 'marks_obtained', 'total_marks', 'remarks']
