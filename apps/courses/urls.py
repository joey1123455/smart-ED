from django.urls import path
from .views import CreateCourseView, create_quiz, news, course_list_view, course_quiz

urlpatterns = [
    path('create/', CreateCourseView.as_view(), name='create_course'),
    path('<str:course_code>/quiz/', create_quiz, name='create_quiz'),
    path('news/', news, name='get_news'),
    path('users/', course_list_view, name='get_courses'),
    path('<str:course_code>/get-quiz/', course_quiz, name='get_quiz'),
]
