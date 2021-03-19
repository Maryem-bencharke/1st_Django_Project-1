from django.shortcuts import render
from .models import articles
from django.utils import timezone

# Create your views here.


def article_list(request):
    all_articles=articles.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    print(all_articles)
    return render(request, 'Home_Page/article_list.html', {'all_articles': all_articles})