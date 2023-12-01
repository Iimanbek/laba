from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import MangaListModel, Afisha, Slider

#Не полная информация
def manga_list_view(request):
    if request.method == "GET":
        manga_list = MangaListModel.objects.all()
        afisha_list = Afisha.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='films/index.html', context={
            'manga_list': manga_list,
            'afisha_list': afisha_list,
            'slider_list': slider_list
        })

#GET ID
def manga_list_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(MangaListModel, id=id)
        return render(request, template_name='films/film_detail.html', context={'film_id': film_id})


