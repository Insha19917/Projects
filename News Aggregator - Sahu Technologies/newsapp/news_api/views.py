from typing import Counter
from django.shortcuts import render
import requests
API_KEY = '92cc48d592a0488ab76afce75484f2a5'

# Create your views here.
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country:
            url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
    else:
            url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']

    context = {
        'articles' : articles
    }
    return render(request,'news_api/home.html', context)