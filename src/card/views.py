from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from card.models import *
import json
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render('index.html', {})

# Return all cards of a company given company name
def get_cards(request):
    company = request.GET.get('company')
    cards = Card.objects.filter(associated_company=company)
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
def add_card(request):
    company_name = request.POST.get('company_name')
    status = request.POST.get('status')
    tags = request.POST.get('tags').split()
    contact_name = request.POST.get('contact_name')
    contact_email = request.POST.get('contact_email')
    contact_phone = request.POST.get('contact_phone')

    new_card = Card(associated_company=company_name, status=status)
    new_card.save()
    new_contact = Company(name=contact_name, phone=contact_phone, email=contact_email, associated_card=new_card)
    new_company.save()
    for tag in tags:
        new_tag = Tag(tag=tag, tagged_card=new_card)
        new_tag.save()
    return JsonResponse({'errCode': 1}, safe=False)

# Add contact given card id and contact info
def add_contact(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    contact_name = request.POST.get('contact_name')
    contact_email = request.POST.get('contact_email')
    contact_phone = request.POST.get('contact_phone')
    new_contact = Company(name=contact_name, phone=contact_phone, email=contact_email, associated_card=card)
    new_company.save()
    return JsonResponse({'errCode': 1}, safe=False)

# Add tags based on card id and tag names
def add_tags(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    tags = request.POST.get('tags').split()
    tags
    for tag in tags:
        new_tag = Tag(tag=tag, tagged_card=card)
        new_tag.save()
    return JsonResponse({'errCode': 1}, safe=False)

# Change status based on card id and new status
def change_status(request):
    card_id = request.GET.get('card_id')
    new_status = request.GET.get('status')
    card = Card.objects.filter(unique_id=card_id)
    if new_status != card.status:
        card.status = new_status
    return JsonResponse({'errCode': 1}, safe=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
