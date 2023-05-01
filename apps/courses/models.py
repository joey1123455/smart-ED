from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from apps.common.models import TimeStampedUUIDModel

user = get_user_model()


class Course(TimeStampedUUIDModel):
    uploaded_by = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    course_code = models.CharField(max_length=7, unique=True)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.course_code

class Question(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return f'{self.question_text} for course {self.course.course_code}'
    


class Answer(TimeStampedUUIDModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.question.course.course_code
    


class Quiz(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.course.course_code
    


class Score(TimeStampedUUIDModel):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.get_username()}' 
