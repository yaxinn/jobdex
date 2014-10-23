from django.shortcuts import render
from card.models import *
import json
from django.core import serializers

# Create your views here.
def home(request):
    return render('index.html', {})

# Return the contact information in JSON given a card ID
def get_contacts(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    contacts = Contact.objects.all().filter(associated_card=card)
    contacts_output = serializers.serialize("json", contacts)
    context = RequestContext(request, {
        'contacts': contacts_output,
    })
    return render('index.html', context)

def add_card(request);
	company_name = request.POST.get('company_name')
	tags = request.POST.get('tags').split()
	contact_name = request.POST.get('contact_name')
	contact_email = request.POST.get('contact_email')
	contact_phone = request.POST.get('contact_phone')

	new_card = Card(associated_company=company_name)
	new_card.save()
	new_contact = Company(name=contact_name, phone=contact_phone, email=contact_email, associated_card=new_card)
	new_company.save()
	for tag in tags:
		new_tag = Tag(tag=tag, tagged_card=new_card)
		new_tag.save()

