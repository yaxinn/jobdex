from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from document.models import *
from user.models import *
from card.models import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models.signals import post_save

# Create your views here.
@csrf_exempt
def upload_document(request):
	name = request.POST['name']
	pdf = request.FILES['pdf']
	# uploaded by maybe not right
	# need to add check for file type 
	user = request.user.profile
	new_document = Document(name=name, pdf=pdf, uploaded_by=request.user.profile)
	new_document.save()
	user.documents.add(new_document)
	user.save()
	return JsonResponse({'error_message': 1}, safe=False)

def remove_document(request):
	try:	
		doc_id = request.DELETE.get('doc_id')
		user = request.user.profile
		user.documents.filter(unique_id=doc_id).delete()
		user.save()
		return JsonResponse({'error_message': 1}, safe=False)
	except Document.DoesNotExist:
		return JsonResponse({'error_message': -11}, safe=False)

def get_documents(request):
	user = request.user.profile
	documents = user.documents.all()
	documents_output = serializers.serialize("json", documents)
	user.save()
	return JsonResponse(documents_output, safe=False)