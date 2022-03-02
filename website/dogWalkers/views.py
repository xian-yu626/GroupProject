from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
	return render(request, 'dogWalkers/dogWalkersPage.html', {})

def walker_list(request):
    posts = Post.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'dogWalkers/dogWalkersPage.html', {'listings':listings})