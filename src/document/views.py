from django.shortcuts import render

# Create your views here.
def post_document(request):
	name = request.POST['name']
	pdf=request.FILES['pdf']
	# uploaded by maybe not right
	new_document = Document(name=name, pdf=pdf, uploaded_by=request.user.profile)
	new_document.save()
	user = request.user.profile
	user.documents.add(new_document)
	user.save()
	