from django.contrib import admin
from tracker.models import User
from tracker.models import Grade
from tracker.models import Assignment
from tracker.models import Student

# Register your models here.
admin.site.register(User)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Assignment)