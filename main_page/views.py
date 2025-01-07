# Create your views here.
from django.shortcuts import render, redirect
from adverts.models import *
import random
from institutions.models import *
from polls.models import *
from events.models import *
from django.utils.timezone import now
from news.models import New
def home_page (request):
    adverts = Advert.objects.all()
    advert_texts = [advert.text for advert in adverts]
    random_advert = random.choice(advert_texts) if advert_texts else None
    request.session['advert'] = random_advert
    inss = Institution.objects.order_by('-rating')[:3]
    polls = Question.objects.order_by('?')[:3]
    events = Event.objects.filter(event_date__gte=now()).order_by('event_date')[:3]
    news = New.objects.filter(published_at__lte=now()).order_by('published_at')[:5]
    return render(
        request,
        template_name="main/home.html",
        context={
            "inss": inss,
            "questions": polls,
            "events": events,
            "news": news,
            }
    )
