from django.shortcuts import render
from .forms import PostulanteForm


def home(request):

    enviado = False


    if request.method == 'POST':

        form = PostulanteForm(request.POST)


        if form.is_valid():

            form.save()

            enviado = True

            form = PostulanteForm()


    else:

        form = PostulanteForm()



    return render(
        request,
        'index.html',
        {
            'form': form,
            'enviado': enviado
        }
    )