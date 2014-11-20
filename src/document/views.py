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
    new_document = Document(doc_name=name, pdf=pdf, uploaded_by=request.user.user_profile)
    new_document.save()
    return JsonResponse({'error_message': 1}, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def delete_document(request):
    try:
        info = json.loads(request.POST.keys()[0])
        doc_id = info['doc_id']
        #user = request.user.user_profile
        #user.documents.filter(unique_id=doc_id).delete()
        #user.save()
        print info
        doc = Document.objects.get(unique_id=doc_id)
        doc.delete()
        return JsonResponse({'error_message': 1}, safe=False)
    except Document.DoesNotExist:
        return JsonResponse({'error_message': -11}, safe=False)

def get_documents(request):
    user = request.user.profile
    documents = user.documents.all()
    documents_output = serializers.serialize("json", documents)
    user.save()
    return JsonResponse(documents_output, safe=False)
