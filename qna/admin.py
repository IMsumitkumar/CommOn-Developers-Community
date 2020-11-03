from django.contrib import admin
from .models import Answer, Question


class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    class Meta:
        model = Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
