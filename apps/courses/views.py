import openai
import json
import requests
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Course, Question, Answer, Quiz
from .serializers import CreateCourseSerializer, CourseSerializer, QuizSerializer
from .helper_functions import parse
from core.settings.base import OPEN_API_KEY



class CreateCourseView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCourseSerializer
    form = """Q3. What is a "man-in-the-middle attack"?
A. An interception of information on an unsecure website
B. A type of encryption
C. A padlock symbol on a website
D. A program that waits in the background
E. A binding connection between a server and browser
Correct Answer: A. An interception of information on an unsecure website
    """
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            course = serializer.save()

            content = course.content
            content = course.content
            quiz = Quiz.objects.create(course=course)
            questions = []
            openai.api_key = f"{OPEN_API_KEY}"
#             form = """Q3. What is a "man-in-the-middle attack"?
# A. An interception of information on an unsecure website
# B. A type of encryption
# C. A padlock symbol on a website
# D. A program that waits in the background
# E. A binding connection between a server and browser
# Correct Answer: A. An interception of information on an unsecure website
#     """
                # Split content into chunks of 1000 characters
            prompt = f"using this format {self.form} Generate 5 multiple choice question and answers and flag thier answers from this text {content}"

        # Use the OpenAI API to generate the question and answers
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=1992,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            # print(response)
            # print(response['choices'][0]['text'])
            string = response['choices'][0]['text'].lstrip()
            q_index = string.find("Q")
            if q_index != -1:
                substring = string[q_index:]
                print("Substring starting from the first 'Q':", substring)
            else:
                print("No 'Q' found in the string.")
            res = parse(substring)
            for i in res:
                # print('hello')
                question = i['question']
                q = Question.objects.create(course=course, question_text=question)
                questions.append(q)
                correct_answer = i['answer']
                answers = i['answers']
                for ans in answers:
                    print(ans)
                    # print(correct_answer[16:].lstrip())
                    if ans.__eq__(correct_answer[16:].lstrip()):
                        print('correct')
                        is_correct = True
                    else:
                        is_correct = False
                    Answer.objects.create(question=q, answer_text=ans, is_correct=is_correct)
            
            quiz.questions.add(*questions)
            

            # Create a new quiz instance with generated questions
            quiz = Quiz.objects.create(course=course)
            quiz.questions.add(*questions)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def course_list_view(request):
    try:
        user = request.user
        print(user)
        courses = Course.objects.filter(uploaded_by=user.pkid)
        print(courses)
        serializer = CourseSerializer(courses, many=True)
    except:
        return Response('User hasnt uploaded any courses', status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def course_quiz(request, course_code):
    
    try:
        quiz = Quiz.objects.filter(course__course_code=course_code)
        serializer = QuizSerializer(quiz, many=True)
    except:
        return Response('User hasnt uploaded any courses', status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def create_quiz(request, course_code):
    try:
        course = Course.objects.get(course_code=course_code)
    
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    content = course.content
    quiz = Quiz.objects.create(course=course)
    questions = []
    openai.api_key = f"{OPEN_API_KEY}"
    form = """Q3. What is a "man-in-the-middle attack"?
A. An interception of information on an unsecure website
B. A type of encryption
C. A padlock symbol on a website
D. A program that waits in the background
E. A binding connection between a server and browser
Correct Answer: A. An interception of information on an unsecure website
"""
            # Split content into chunks of 1000 characters
    prompt = f"using this format {form} Generate 5 multiple choice question and answers and flag thier answers from this text {content}"

    # Use the OpenAI API to generate the question and answers
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1992,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # print(response)
    # print(response['choices'][0]['text'])
    res = parse(response['choices'][0]['text'].lstrip())
    for i in res:
        # print('hello')
        question = i['question']
        q = Question.objects.create(course=course, question_text=question)
        questions.append(q)
        correct_answer = i['answer']
        answers = i['answers']
        for ans in answers:
            print(ans)
            # print(correct_answer[16:].lstrip())
            if ans.__eq__(correct_answer[16:].lstrip()):
                print('correct')
                is_correct = True
            else:
                is_correct = False
            Answer.objects.create(question=q, answer_text=ans, is_correct=is_correct)
    
    quiz.questions.add(*questions)

    return Response({'success': 'Quiz created successfully'}, status=status.HTTP_201_CREATED)


def news(request):
    if request.method == 'GET':
        url = f"https://newsapi.org/v2/everything?q=scholarship offers&apiKey=85f9b07a8b1d4fc4b1005b6adc77a9bb"
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        j = {}
        x = 0
        for i in articles:
            source = i['source']['name']
            article_title = i['title']
            j[x] = {'source': source,
            'author': i['author'],
            'title': article_title,
            'image_url': i['urlToImage'],
            'post_url': i['url'],
            'description': i['description']}
            x += 1
            
        return JsonResponse({"article_list": j}, status=200)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)