from django.shortcuts import render, redirect
from .models import Jogador
from .forms import JogadorForm
from django.http import HttpResponse
from django.template import loader


def index(request):
     template = loader.get_template('index.html')
     context = {}
     return HttpResponse(template.render(context, request))

     
def jogadorList(request):  
   jogadores = Jogador.objects.all()  
   return render(request,"jogador-list.html",{'jogadores':jogadores})  

def jogadorCreate(request):  
    if request.method == "POST":  
        form = JogadorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('jogador-list')  
            except:  
                pass  
    else:  
        form = JogadorForm()  
    return render(request,'jogador-create.html',{'form':form})  

def jogadorDelete(request, idjogador):
    jogador = Jogador.objects.get(idjogador = idjogador)
    try:
        jogador.delete()
    except:
        pass
    return redirect('jogador-list')

def jogadorUpdate(request, idjogador):
    jogador = Jogador.objects.get(idjogador=idjogador)
    form = JogadorForm(initial={
        'idjogador': jogador.idjogador,
        'nome': jogador.nome,
        'login': jogador.login,
        'senha': jogador.senha
    }) 
    if request.method == "POST":
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            try:
                form.save()
                return redirect('jogador-list')
            except Exception as e:
                return render(request, 'jogador-update.html', {'form': form, 'error': str(e)})
    return render(request, 'jogador-update.html', {'form': form})

