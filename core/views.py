from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, AttendanceForm, ResultForm
from .models import Attendance, Result, Fee, StudentProfile, TeacherProfile, Classroom, Subject


from .forms import CustomUserCreationForm, AttendanceForm, ResultForm
from .models import Attendance, Result, Fee, StudentProfile, TeacherProfile, Classroom, Subject
def home(request):
    return render(request, "core/home.html")
def home(request):
    return HttpResponse("School ERP System is Live 🚀")
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    context = {}
    if request.user.is_student:
        student = request.user.student_profile
        context['attendance_count'] = student.attendances.filter(status='Present').count()
        context['total_attendance'] = student.attendances.count()
        context['recent_results'] = student.results.all().order_by('-exam_date')[:5]
        context['pending_fees'] = student.fees.filter(is_paid=False)
        return render(request, 'core/student_dashboard.html', context)
    
    elif request.user.is_teacher:
        teacher = request.user.teacher_profile
        classrooms = Classroom.objects.all()
        context['total_students'] = StudentProfile.objects.count()
        context['classrooms'] = classrooms
        # Data for chart: Student distribution per class
        context['class_names'] = [c.name for c in classrooms]
        context['class_student_counts'] = [c.students.count() for c in classrooms]
        return render(request, 'core/teacher_dashboard.html', context)
    
    else:
        # Admin dashboard
        context['total_students'] = StudentProfile.objects.count()
        context['total_teachers'] = TeacherProfile.objects.count()
        context['total_fees_collected'] = sum(f.amount for f in Fee.objects.filter(is_paid=True))
        context['classroom_count'] = Classroom.objects.count()
        return render(request, 'core/admin_dashboard.html', context)

# Attendance Views
@login_required
def attendance_list(request):
    if not (request.user.is_teacher or request.user.is_admin):
        return redirect('dashboard')
    
    attendances = Attendance.objects.all().order_by('-date')
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            if request.user.is_teacher:
                attendance.recorded_by = request.user.teacher_profile
            attendance.save()
            messages.success(request, 'Attendance recorded!')
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    
    return render(request, 'core/attendance_list.html', {'attendances': attendances, 'form': form})

@login_required
def delete_attendance(request, pk):
    if not (request.user.is_teacher or request.user.is_admin):
        return redirect('dashboard')
    attendance = get_object_or_404(Attendance, pk=pk)
    attendance.delete()
    messages.warning(request, 'Attendance record deleted.')
    return redirect('attendance_list')

# Result Views
@login_required
def result_list(request):
    if not (request.user.is_teacher or request.user.is_admin):
        return redirect('dashboard')
    
    results = Result.objects.all().order_by('-exam_date')
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            if request.user.is_teacher:
                result.recorded_by = request.user.teacher_profile
            result.save()
            messages.success(request, 'Result recorded!')
            return redirect('result_list')
    else:
        form = ResultForm()
        
    return render(request, 'core/result_list.html', {'results': results, 'form': form})

# Student Specific Views
@login_required
def student_attendance(request):
    if not request.user.is_student:
        return redirect('dashboard')
    attendances = request.user.student_profile.attendances.all().order_by('-date')
    return render(request, 'core/student_attendance.html', {'attendances': attendances})

@login_required
def student_results(request):
    if not request.user.is_student:
        return redirect('dashboard')
    results = request.user.student_profile.results.all().order_by('-exam_date')
    return render(request, 'core/student_results.html', {'results': results})

@login_required
def student_fees(request):
    if not request.user.is_student:
        return redirect('dashboard')
    fees = request.user.student_profile.fees.all()
    return render(request, 'core/student_fees.html', {'fees': fees})
