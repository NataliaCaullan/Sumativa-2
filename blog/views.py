from django.shortcuts import render
from .models import Post, Category, Hashtag

def index(request):
    # Obtén todos los hashtags y categorías
    categorias = Category.objects.all()
    hashtags = Hashtag.objects.all()

    # Obtén la categoría seleccionada (si existe) de la URL
    categoria_seleccionada = request.GET.get('categoria')

    # Obtén el hashtag seleccionado (si existe) de la URL
    hashtag_seleccionado = request.GET.get('hashtag')

    # Filtra las publicaciones según la categoría y el hashtag seleccionado
    publicaciones = Post.objects.all().order_by('-fecha')

    if categoria_seleccionada:
        print("Categoría seleccionada:", categoria_seleccionada)
        publicaciones = publicaciones.filter(categoria__nombre=categoria_seleccionada)

    if hashtag_seleccionado:
        publicaciones = publicaciones.filter(etiquetas__nombre=hashtag_seleccionado)

    context = {
        'publicaciones': publicaciones,
        'categorias': categorias,
        'hashtags': hashtags,
    }

    return render(request, 'blog.html', context)
