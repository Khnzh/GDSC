from django.db import models
from datetime import date
from google.cloud import texttospeech

def synthesize_text(text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    a_path = f"/home/robi/DjangoApp/src/GDSC/testproject/static/{output_file}"

    with open(f"{a_path}", "wb") as out:
        out.write(response.audio_content)
    return a_path
# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=date(2023, 12, 28))
    price = models.FloatField()
    duration = models.IntegerField()
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    min_age = models.IntegerField()
    destination = models.CharField(max_length=50)
    audio_desc = models.FileField( upload_to =  'static/', default='tests.py')
    audio_price = models.FileField( upload_to =  'static/', default='tests.py')
    audio_name = models.FileField( upload_to =  'static/', default='tests.py')
    
    def save(self, *args, **kwargs):
        # Your custom logic to determine the value of field2 based on field1
        a_path = synthesize_text(self.description, f"{self.id}.wav")
        with open(a_path, 'rb') as audio_file:
            self.audio_desc.save(f"{self.id}.wav", audio_file, save=False)

        a_path = synthesize_text(f"Total price is {self.price} euros", f"{self.id}.wav")
        with open(a_path, 'rb') as audio_file:
            self.audio_price.save(f"{self.id}.wav", audio_file, save=False)

        a_path = synthesize_text(f"Tour name is {self.name}", f"{self.id}.wav")
        with open(a_path, 'rb') as audio_file:
            self.audio_name.save(f"{self.id}.wav", audio_file, save=False)
        # self.calculate_field2()

        super().save(*args, **kwargs)

class Guide(models.Model):
    name = models.CharField(max_length=50, default="Miguel")
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    experience = models.IntegerField()
    sp_english = models.BooleanField()
    sp_georgian = models.BooleanField()
    sp_spanish = models.BooleanField()
    sp_japanese = models.BooleanField()
    image = models.CharField(max_length=50)
    tours = models.ManyToManyField(Tour)

class YourModel(models.Model):
    field1 = models.CharField(default="take your dream and hold it as it is your life", max_length = 200)
    field2 = models.FileField( upload_to =  'static/', default='tests.py')

    # def save(self, *args, **kwargs):
    #     # Your custom logic to determine the value of field2 based on field1
    #     a_path = synthesize_text(self.field1, f"{self.id}.wav")
    #     with open(a_path, 'rb') as audio_file:
    #         self.field2.save(f"{self.id}.wav", audio_file, save=False)
    #     # self.calculate_field2()

    #     super().save(*args, **kwargs) 

