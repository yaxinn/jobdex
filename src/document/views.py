from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from document.models import *
from user.models import *
from card.models import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models.signals import post_save
import json


def report(request):
    context = {"documents": Document.objects.all()}
    return render(request, 'report.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def upload_document(request):
    name = request.POST['name']
    pdf = request.FILES['pdf']
    user = request.user.user_profile
    if str(pdf).split(".")[-1] != "pdf":
        return JsonResponse({'error_message': -10}, safe=False)
    try:
        Document.objects.get(doc_name=name)
        return JsonResponse({'error_message': -9}, safe=False)
    except Document.DoesNotExist:
        new_document = Document(doc_name=name, pdf=pdf, uploaded_by=request.user.user_profile)
        new_document.save()
        return JsonResponse({'error_message': 1}, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def delete_document(request):
    try:
        # uncomment the following two lines when not testing 
        info = json.loads(request.POST.keys()[0])
        doc_id = info['doc_id']
        ########################

        #user = request.user.user_profile
        #user.documents.filter(unique_id=doc_id).delete()
        #user.save()

        # for testing purpose, use the following line, comment it out when done with testing
        # doc_id = request.POST['doc_id']
        ########################

        doc = Document.objects.get(unique_id=doc_id)
        doc.delete()
        return JsonResponse({'error_message': 1}, safe=False)
    except Document.DoesNotExist:
        return JsonResponse({'error_message': -11}, safe=False)

def get_documents(request):
    user = request.user.user_profile
    documents = Document.objects.all().filter(uploaded_by=user)
    documents_output = {}
    for document in documents:
        doc = {}
        doc['date_uploaded'] = document.date_uploaded
        doc['url'] = document.pdf.url
        doc['unique_id'] = document.unique_id
        documents_output[document.doc_name] = doc
    return JsonResponse(documents_output, safe=False)

