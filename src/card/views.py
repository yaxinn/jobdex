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
    #print request.user.username
    if request.user.is_active and request.user.is_authenticated:
        cards = Card.objects.filter(owner=request.user)
        return render(request, 'index.html', {"cards": cards})
    return render(request, 'index.html', {})

def about(request):
    context = {}
    return render(request, 'about.html', context)

def report(request):
    context = {}
    return render(request, 'report.html', context)

def get_all_cards(request):
    cards = Card.objects.all()
    cards_output = serializers.serialize("json", cards)
    return JsonResponse(cards_output, safe=False)

# Return all cards of a company, given company name
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

# Remove contact, given a card id and contact name
def remove_contact(request):
    try:
        card_id = request.GET.get('card_id')
        contact_name = request.DELETE.get('contactName')
        Contact.objects.filter(name=contact_name, tagged_card=card_id).delete()
        return JsonResponse({'error_message': 1}, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)
    except Contact.DoesNotExist:
        return JsonResponse({'error_message': -14}, safe=False)

# Edit a contact, given a card id and contact fields (not all fields may be overridden, depending on what user edits)
@csrf_exempt
def edit_contact(request):
    try:
        card_id = request.GET.get('card_id')
        contact_name = request.POST.get('contactName')
        contact_email = request.POST.get('contactEmail')
        contact_phone = request.POST.get('contactPhone')
        contact_title = request.POST.get('contactTitle')
        contact = Contact.objects.filter(name=contact_name, tagged_card=card_id)
        contact.name = contact_name
        contact.email = contact_email
        contact.phone = contact_phone
        contact.title = contact_title
        contact.save()
        return JsonResponse({'error_message': 1}, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)
    except Contact.DoesNotExist:
        return JsonResponse({'error_message': -14}, safe=False)

# Add card given company name, status, tags, and contact info
@csrf_exempt
def create_card(request):
    info = json.loads(request.POST.keys()[0])
    company_name = info['companyName']
    status = str(info['status'])
    job_title = info['jobTitle']
    notes = str(info['notes'])
    tags = str(info['tags']).split(',')
    contact_name = str(info['contactName'])
    contact_email = str(info['contactEmail'])
    contact_phone = str(info['contactPhone'])
    user = UserProfile.objects.get(username=request.user)

    try:
        company = Company.objects.get(name=company_name)
    except Company.DoesNotExist:
        company = Company(name=company_name)
        company.save()

    new_card = Card(associated_company=company, status=status, job_title=job_title, notes=notes, owner=user)
    new_card.save()

    new_contact = Contact(name=contact_name, phone=contact_phone, email=contact_email, associated_card=new_card)
    new_contact.save()

    for tag in tags:
        new_tag = Tag(tag=tag.strip(), tagged_card=new_card)
        new_tag.save()
    card_id = str(new_card.unique_id)
    response = {'card_id': card_id, 'error_message': 1}
    return JsonResponse(response, safe=False)




# Remove card, given a card id
@csrf_exempt
def remove_card(request):
    try:
        info = json.loads(request.POST.keys()[0])
        card_id = info['card_id']
        Card.objects.filter(unique_id=card_id).delete()
        return JsonResponse({'error_message': 1}, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)

# Add contact given card id and contact info
@csrf_exempt
def add_contact(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    contact_name = request.POST.get('contact_name')
    contact_email = request.POST.get('contact_email')
    contact_phone = request.POST.get('contact_phone')
    contact_title = request.POST.get('contact_title')
    new_contact = Company(name=contact_name, phone=contact_phone, email=contact_email, title=contact_title, associated_card=card)
    new_contact.save()
    return JsonResponse({'error_message': 1}, safe=False)

# Add tags based on card id and tag names
@csrf_exempt
def add_tag(request):
    card_id = request.GET.get('card_id')
    card = Card.objects.filter(unique_id=card_id)
    tags = request.POST.get('tags').split(',')
    for tag in tags:
        new_tag = Tag(tag=tag, tagged_card=card)
        new_tag.save()
    return JsonResponse({'error_message': 1}, safe=False)

# Remove tag or set of tags, given a card id and tag name(s)
def remove_tag(request):
    try:
        card_id = request.GET.get('card_id')
        tags = request.DELETE.get('tags').split(',')
        for tag in tags:
            Tag.objects.filter(tag=tag, tagged_card=card_id).delete()
        return JsonResponse({'error_message': 1}, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)
    except Tag.DoesNotExist:
        return JsonResponse({'error_message': -3}, safe=False)

# Get all tags associated with a card id
def get_tags(request):
    try:
        card_id = request.GET.get('card_id')
        card = Card.objects.filter(unique_id=card_id)
        tags = Tag.objects.all().filter(tagged_card=card)
        tags_output = serializers.serialize("json", tags)
        return JsonResponse(tags_output, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)
    except Tag.DoesNotExist:
        return JsonResponse({'error_message': -3}, safe=False)

# Modify a tag, given a card id and tag name
@csrf_exempt
def modify_tag(request):
    try:
        card_id = request.GET.get('card_id')
        old_tag = request.GET.get('old_tag')
        new_tag = request.POST.get('new_tag')
        card = Card.objects.filter(unique_id=card_id)
        tags = Tag.objects.filter(tagged_card=card_id)
        for tag in tags:
            if tag == old_tag:
                tag = new_tag
                tag.save()
        return JsonResponse({'error_message': 1}, safe=False)
    except Card.DoesNotExist:
        return JsonResponse({'error_message': -8}, safe=False)
    except Tag.DoesNotExist:
        return JsonResponse({'error_message': -3}, safe=False)

# Change status based on card id and new status
@csrf_exempt
def modify_card_status(request):
    card_id = request.GET.get('card_id')
    new_status = request.POST.get('status')
    card = Card.objects.filter(unique_id=card_id)
    if new_status != card.status:
        card.status = new_status
        card.save()
    return JsonResponse({'error_message': 1}, safe=False)

#class UserProfile(models.Model):
#    user = models.OneToOneField(User, related_name="profile")
#
#    def __str__(self):
#        return "%s's profile" % self.user
#
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        profile, created = user.models.UserProfile.objects.get_or_create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)
