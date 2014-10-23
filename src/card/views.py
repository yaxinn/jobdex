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
