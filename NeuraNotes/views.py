from django.shortcuts import render,redirect
from django.http import JsonResponse
from .ai_utils import summarize_note,grammar_check, title_generator,tag_generator,polish_generator
from rest_framework.decorators import api_view
from .models import Note
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def note(request):
    if request.method == "POST":
        title = request.POST.get("title1")
        content = request.POST.get("content1")

        if title and content:
            obj = Note(user=request.user, title=title, content=content)
            obj.save()
            
        return redirect("dashboard")

    return render(request, 'note.html')

@login_required(login_url="login")
def editnotes(request,id):
     Notes = Note.objects.get(id=id, user=request.user)
     if request.method == 'POST':
        Notes.title = request.POST.get('title1')
        Notes.content = request.POST.get('content1')
        Notes.ai_title = request.POST.get('ai_title1', '')
        Notes.ai_summary = request.POST.get('ai_summary1', '')
        Notes.ai_grammar = request.POST.get('ai_grammar1', '')
        Notes.save()
        return redirect('dashboard')
     context = {
         'Notes': Notes
     }
     return render(request, 'note.html', context)
     
@login_required(login_url="login")
def delete_note(request, id):
    note = Note.objects.get(id=id, user=request.user)
    note.delete()
    return redirect('/dashboard/')


@login_required(login_url="login")
def dashboard(request):
    notes = Note.objects.filter(user=request.user).order_by("-created_at")
    total_count = notes.count()
    context = {
        'data': notes,
        'notes': notes,
        'total_count': total_count,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url="login")
def summarize_page(request):
    return render(request, 'summarize_note.html')

@login_required(login_url="login")
def grammar_page(request):
    return render(request, 'grammer.html')

@login_required(login_url="login")
def title_gen_page(request):
    return render(request, 'title_gen.html')

@login_required(login_url="login")
def tag(request):
    return render(request,'tag.html')

@login_required(login_url="login")   
def polish(request):
    return render(request,'polish.html')

@api_view(['POST'])
def summarize(request):
    note = request.data.get("note")
    summary = summarize_note(note)
    return Response({"result":summary})

@api_view(['POST'])
def grammar(request):
    note = request.data.get("note")
    grammer = grammar_check(note)
    return Response({"result":grammer}) 

@api_view(['POST'])
def title_gen(request):
    note = request.data.get("note")
    title = title_generator(note)
    return Response({"result":title}) 

@api_view(['POST'])
def tag_gen(request):
    note = request.data.get("note")
    tag = tag_generator(note)
    return Response({"result":tag})

@api_view(['POST'])
def polish_gen(request):
    note = request.data.get("note")
    polish = polish_generator(note)
    return Response({"result":polish})
