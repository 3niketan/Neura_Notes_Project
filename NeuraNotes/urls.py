from django.urls import path

from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("note/", views.note, name="note"),
    path("note/<int:id>/edit/", views.editnotes, name="editnotes"),
    path("note/<int:id>/delete/", views.delete_note, name="delete_note"),
    path("summarize/", views.summarize_page, name="summarize_page"),
    path("grammar/", views.grammar_page, name="grammar_page"),
    path("title_gen/", views.title_gen_page, name="title_gen_page"),
    path("auto_tag/", views.tag, name="tag_page"),
    path("rewrite_polish/", views.polish, name="polish_page"),
    path('ai/summarize/', views.summarize, name='summarize'),
    path('ai/grammar/', views.grammar, name='grammar'),
    path('ai/title_generator/', views.title_gen, name='title'),
    path('ai/tag_generator/', views.tag_gen, name='tag'),
    path('ai/polish_generator/', views.polish_gen, name='polish'),
]
