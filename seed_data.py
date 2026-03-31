import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_erp.settings')
django.setup()

from core.models import Classroom, Subject, User

def populate():
    # Create Classrooms
    c1, _ = Classroom.objects.get_or_create(name="Grade 10", section="A")
    c2, _ = Classroom.objects.get_or_create(name="Grade 10", section="B")
    c3, _ = Classroom.objects.get_or_create(name="Grade 11", section="Medical")
    
    # Create Subjects
    Subject.objects.get_or_create(name="Mathematics", code="MATH101", classroom=c1)
    Subject.objects.get_or_create(name="Physics", code="PHY101", classroom=c1)
    Subject.objects.get_or_create(name="Biology", code="BIO111", classroom=c3)
    
    # Create Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created with password 'admin123'")

if __name__ == "__main__":
    populate()
    print("Database populated with initial classrooms and subjects.")
