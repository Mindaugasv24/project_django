from django.contrib import admin
from .models import Person, Exam, Question, Examquestion, Answer, Result


class ChoiceInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Person)
admin.site.register(Exam)
admin.site.register(Question, QuestionsAdmin)
admin.site.register(Examquestion)
admin.site.register(Answer)
admin.site.register(Result)
