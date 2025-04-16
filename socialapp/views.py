from django.shortcuts import render, redirect
from .models import Postagem
from .forms import PostagemForm


# Create your views here.

def index(request):
    return render(request, 'social/index.html')

def contato(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')
    return render(request, 'social/contact.html', {'postagens': postagens})

def nova_postagem(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('social/index.html')  # nome da url da home
    else:
        form = PostagemForm()
    return render(request, 'social/contact.html', {'form': form})

def sobre(request):
    return render(request, 'social/about.html')

def postar(request):
    return render(request, 'social/post.html')

def base(request):
    return render(request, 'social/base.html')