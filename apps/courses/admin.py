from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['uploaded_by', 'course_code', 'name']
    list_filter = ['course_code', 'name', 'uploaded_by']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'question_text']
    list_filter = ['course', 'question_text']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer_text', 'is_correct']
    list_filter = ['question', 'answer_text', 'is_correct']


class ScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score']
    list_filter = ['user', 'quiz', 'score']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['course',]
    list_filter = ['course',]


admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Quiz, QuizAdmin)