from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json 
from pprint import pprint 
from textblob import TextBlob
from django.http import JsonResponse

@api_view(["POST"])
def index(request):
    subjective_sentences = []
    nonsubjective_sentences = []
    text = request.POST.get("text")


    for sentence in text.split("."):
        tb = TextBlob(sentence)
        analysis = tb.sentiment
        if(analysis.subjectivity>=0.6):
            subjective_sentences.append(sentence)
        else:
            nonsubjective_sentences.append(sentence)
    
    # pprint("Subjective Sentences : {}".format(subjective_sentences))

    # pprint("Non subjective Sentences : {}".format(nonsubjective_sentences))
    response = {
        'subjective': subjective_sentences,
        'nonsubjective': nonsubjective_sentences
    }
    return JsonResponse(response)
    # return HttpResponse(json.dumps(response))
