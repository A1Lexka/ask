from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question 
from qa.models import Answer
from .forms import AskForm, AnswerForm
from django.views.decorators.csrf import csrf_exempt


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

#@require_GET
@csrf_exempt
def question_details(request, question_id):
    if request.method == "POST":
        return question_add(request)
    form = AnswerForm(initial={'question': question_id})
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/questioned.html', {
        'question': question,
        'title': question.title,
        'text': question.text,
        'answers': answers.all()[:],
        'form': form,
    })

@csrf_exempt    
def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
    #        url = post.get_url()
            url = "/question/"
            adds = str(post.id)
            return HttpResponseRedirect(url + adds)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {'form': form})

def answer(request):
    if request.method == "POST":
        form = AnswerForm(initial={'question': question_id})
        return render(request, 'qa/questioned.html', {
        'question': question,
        'title': question.title,
        'text': question.text,
        'answers': answers.all()[:],
        'form': form,
    })
    return HttpResponseRedirect("/poni/")         








