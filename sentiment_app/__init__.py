from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model and vectorizer once
model = joblib.load(os.path.join(BASE_DIR, 'svm_model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl'))

def index(request):
    return render(request, 'sentiment_app/index.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        processed_text = text.lower().strip()
        X = vectorizer.transform([processed_text])
        prediction = model.predict(X)[0]
        label_map = {0: "negatif", 1: "positif"}
        result = label_map.get(prediction, str(prediction))
        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'}, status=400)
