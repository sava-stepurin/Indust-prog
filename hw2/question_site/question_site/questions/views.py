from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone


from .models import Question
from .models import QuestionForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            q = Question(question_text=request.POST['question_text'], pub_date=timezone.now())
            q.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'questions/index.html', {'form': form,
            'latest_question_list': latest_question_list})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'questions/index.html', {'form': form,
    'latest_question_list': latest_question_list})
