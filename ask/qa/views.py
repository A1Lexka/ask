from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question 
from qa.models import Answer

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)

def questions_all(request):
    questions = Question.objects.order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)   
    return render(request, 'qa/all.html', {
        'questions': page.object_list,
    #    'title': question.title,
        'paginator': paginator, 'page': page})

#WORKING
#def questions_all(request):
#    questions = Question.objects.all()
#    return render(request, 'qa/all.html', {'questions': questions})

def popular_questions(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/all.html', {
        'questions': page.object_list,
        #title: questions.title,
        'paginator': paginator, page: page,})    

@require_GET
def question_details(request, question_id):
#    try:
#        question = Question.objects.get(question_id=question_id)
#    except Question.DoesNotExist:
#        raise Http404
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', {
        'question': question,
        'title': question.title,
        'text': question.text,
        'answers': answers.all()[:],    })

    
