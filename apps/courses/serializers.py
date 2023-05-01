from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Course, Quiz, Question, Answer, Score

USER = get_user_model()

class CourseSerializer(serializers.ModelSerializer):
    #uploaded_by = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'name', 'course_code', 'content']

    # def get_user(self, obj):
    #     return obj.user.username


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answers']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'questions']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'user', 'quiz', 'score']


class UpdateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'content']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [ 'name', 'course_code', 'content']

    def create(self, validated_data):
        user = self.context['request'].user
        course = Course.objects.create(
            uploaded_by=user,
            name=validated_data['name'],
            course_code=validated_data['course_code'],
            content=validated_data['content']
        )
        return course