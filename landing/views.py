from django.shortcuts import render,redirect
from .models import ContactMessage
from authentication.models import EventPhoto,Sponsors
from django.contrib import messages  # For success messages

def home(request):
    sports = EventPhoto.objects.filter(category='sports')
    arts = EventPhoto.objects.filter(category='arts')
    tech = EventPhoto.objects.filter(category='tech')
    cultural = EventPhoto.objects.filter(category='cultural')
    sponsors = Sponsors.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            
    return render(request, "landing/index.html", {
        "sports": sports,
        "arts":arts,
        "tech":tech,
        "cultural": cultural,
        "sponsors":sponsors,
        
        })


import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from PIL import Image
from io import BytesIO
import base64
import os
import json
genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

@csrf_exempt
def chatbot(request):
    """API to handle chatbot responses using Google Gemini."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "Hello!")

            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(user_message)

            ai_reply = response.text if response.text else "Sorry, I couldn't generate a response."

            return JsonResponse({"status": "success", "reply": ai_reply})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method."})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def generate_image(request):
    try:
        # Parse the request body
        data = json.loads(request.body)
        user_prompt = data.get('prompt', '')
        
        if not user_prompt:
            return JsonResponse({"error": "No prompt provided"}, status=400)
        
        # NVIDIA API configuration
        invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"
        
        headers = {
            "Authorization": "Bearer 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",
            "Accept": "application/json",
        }
        
        # Prepare the payload using the user input
        payload = {
            "text_prompts": [
                {
                    "text": user_prompt,
                    "weight": 1
                },
                {
                    "text": "blurry, low quality, distorted, ugly",
                    "weight": -1
                }
            ],
            "cfg_scale": 7,
            "sampler": "K_DPM_2_ANCESTRAL",
            "seed": 0,
            "steps": 30
        }
        
        # Make the request to NVIDIA API
        response = requests.post(invoke_url, headers=headers, json=payload)
        response.raise_for_status()
        response_body = response.json()
        
        # Return the API response as JSON
        return JsonResponse(response_body)
        
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)