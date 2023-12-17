from django.shortcuts import render
from google.cloud import texttospeech
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Test
from django.views import generic
import logging
from .models import Tour, Guide
from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, "base.html", {"message":"message"})

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context['message'] = "User already exists."
            return render(request, 'onlinecourse/user_registration_bootstrap.html', context)

def login_request(request):
    context = {}
    if request.method == "POST":
        # print(request.body)
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

@csrf_exempt    
def tours_list(request):
    if request.method == "POST":
        print(request.body)
        # new = Test.objects.get(id=1)
        # new.field1 = str(request.POST['name'])
        return HttpResponseRedirect(reverse('index'))
    context = {}
    context['tours']=Tour.objects.all()
    return render(request, 'tours.html', context)


# class ToursListView(generic.ListView):
#     template_name = 'tours.html'
#     context_object_name = 'tours_list'
    
#     def get_queryset(self):
#         user = self.request.user
#         tours = Tour.objects.all()
#         return tours

    
class GuidesListView(generic.ListView):
    template_name = 'guides.html'
    context_object_name = 'guides_list'

    def get_queryset(self):
        user = self.request.user
        guides = Guide.objects.all()
        return guides
    
# def text_to_speech(request):
#     # Get the text to be converted to speech
#     # text = request.GET.get('text', '')
#     text = r"---"
#     # Initialize the Text-to-Speech client
#     client = texttospeech.TextToSpeechClient()

#     # Set the text input
#     synthesis_input = texttospeech.SynthesisInput(text=text)

#     # Set the voice parameters
#     voice = texttospeech.VoiceSelectionParams(
#         language_code='en-US',  # Change this based on your language preference
#         name='en-US-Wavenet-D',  # Change this based on your voice preference
#     )

#     # Set the audio parameters
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.LINEAR16
#     )

#     # Call the Text-to-Speech API
#     response = client.synthesize_speech(
#         input=synthesis_input, voice=voice, audio_config=audio_config
#     )

#     # Send the generated audio file as the HTTP response
#     return HttpResponse(response.audio_content, content_type="audio/wav")