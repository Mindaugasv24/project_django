from django.contrib import admin
from .models import Person, Exam, Question

admin.site.register(Person)
admin.site.register(Exam)
admin.site.register(Question)
# admin.site.register(Examquestion)
# admin.site.register(Answer)
# admin.site.register(Result)
