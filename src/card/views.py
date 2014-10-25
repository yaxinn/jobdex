from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_save
from card.models import *
from user.models import *
from document.models import *
import json
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Home page view
def home(request):
    return render(request, 'index.html', {})

# Return all cards of a company given company name
def get_company_cards(request):
    company_name = request.GET.get('company_name')
    cards = Card.objects.filter(associated_company=company_name)
    cards_output = serializers.serialize("json", cards)
    return JsonResponse(cards_output, safe=False)

# Return the contact information in JSON given a card ID
def get_contacts(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    contacts = Contact.objects.all().filter(associated_card=card)
    contacts_output = serializers.serialize("json", contacts)
    return JsonResponse(contacts_output, safe=False)

# Add card given company name, status, tags, and contact info
@csrf_exempt
def create_card(request):
    info = json.loads(request.POST.keys()[0])
    company_name = info['companyName']
    status = str(info['status'])
    job_title = info['jobTitle']
    tags = str(info['tags'])
    contact_name = str(info['contactName'])
    contact_email = str(info['contactEmail'])
    contact_phone = str(info['contactPhone'])

    try:
        company = Company.objects.get(name=company_name)
    except Company.DoesNotExist:
        company = Company(name=company_name)
        company.save()

    new_card = Card(associated_company=company, status=status, job_title=job_title)
    new_card.save()

    new_contact = Contact(name=contact_name, phone=contact_phone, email=contact_email, associated_card=new_card)
    new_contact.save()

    for tag in tags:
        new_tag = Tag(tag=tag, tagged_card=new_card)
        new_tag.save()
    # Not sure if we should return the id so javascript can store it or just errorCode
    card_id = str(new_card.unique_id)
    # card_id_output = serializers.serialize("json", card_id)
    response = {'card_id': card_id, 'error_message': 1}
    return JsonResponse(response, safe=False)
    #return JsonResponse({'error_message': 1}, safe=False)

# Add contact given card id and contact info
def add_contact(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    contact_name = request.POST.get('contact_name')
    contact_email = request.POST.get('contact_email')
    contact_phone = request.POST.get('contact_phone')
    new_contact = Company(name=contact_name, phone=contact_phone, email=contact_email, associated_card=card)
    new_company.save()
    return JsonResponse({'error_message': 1}, safe=False)

# Add tags based on card id and tag names
def add_tag(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    tags = request.POST.get('tags').split(',')
    for tag in tags:
        new_tag = Tag(tag=tag, tagged_card=card)
        new_tag.save()
    return JsonResponse({'error_message': 1}, safe=False)

# Change status based on card id and new status
def modify_card_status(request):
    card_id = request.GET.get('card_id')
    new_status = request.GET.get('status')
    card = Card.objects.filter(unique_id=card_id)
    if new_status != card.status:
        card.status = new_status
    return JsonResponse({'error_message': 1}, safe=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
