from django.shortcuts import render, redirect, get_object_or_404
from Banca.forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def viewBanci(request):
    banciList = Banci.objects.order_by('nume')
    banciDict = {'banci': banciList}
    return render(request, 'banci.html', context=banciDict)


def viewSucursale(request):
    sucursaleList = Sucursale.objects.order_by('nume')
    sucursaleDict = {'sucursale': sucursaleList}
    return render(request, 'sucursale.html', context=sucursaleDict)


def viewAngajati(request):
    angajati_list = Angajati.objects.order_by('nume')
    angajatiDict = {'angajati': angajati_list}
    return render(request, 'angajati.html', context=angajatiDict)


def addBanca(request):
    if request.method == 'POST':
        bancaForm = BancaForm(request.POST)
        if bancaForm.is_valid():
            bancaForm.save()
            messages.success(request, 'Banca adaugata')
        else:
            messages.error(request, 'Adaugare nereusita')

        return redirect('/banci')

    bancaForm = BancaForm()
    banci = Banci.objects.all()
    return render(request, 'adaugareBanca.html',
                  context={'bancaForm': bancaForm,
                           'banci': banci})


def addSucursala(request):
    if request.method == 'POST':
        sucursalaForm = SucursalaForm(request.POST)
        if sucursalaForm.is_valid():
            sucursalaForm.save()
            messages.success(request, 'Sucursala adaugata')
        else:
            messages.error(request, 'Adaugare nereusita')

        return redirect('/sucursale')

    sucursalaForm = SucursalaForm()
    sucursale = Sucursale.objects.all()
    return render(request, 'adaugareSucursala.html',
                  context={'sucursalaForm': sucursalaForm,
                           'sucursale': sucursale})


def addAngajat(request):
    if request.method == 'POST':
        angajatForm = AngajatForm(request.POST)
        if angajatForm.is_valid():
            angajatForm.save()
            messages.success(request, 'Angajat adaugat')
        else:
            messages.error(request, 'Adaugare nereusita')

        return redirect('/angajati')

    angajatForm = AngajatForm()
    angajati = Angajati.objects.all()
    return render(request, 'adaugareAngajat.html',
                  context={'angajatForm': angajatForm,
                           'angajati': angajati})


def editBanca(request, id):
    banca = get_object_or_404(Banci, id=id)
    if request.method == 'POST':
        sucursalaForm = BancaForm(request.POST, instance=banca)
        if sucursalaForm.is_valid():
            sucursalaForm.save()
            return redirect('/banci')
    else:
        sucursalaForm = BancaForm(instance=banca)

    bancaForm = BancaForm()
    return render(request, 'editareBanca.html',
                  {
                      'bancaForm': bancaForm,
                      'banca': banca,
                  })


def editSucursala(request, id):
    sucursala = get_object_or_404(Sucursale, id=id)
    if request.method == 'POST':
        sucursalaForm = SucursalaForm(request.POST, instance=sucursala)
        if sucursalaForm.is_valid():
            sucursalaForm.save()
            return redirect('/sucursale')
    else:
        sucursalaForm = SucursalaForm(instance=sucursala)

    sucursalaForm = SucursalaForm()
    return render(request, 'editareSucursala.html',
                  {
                      'sucursalaForm': sucursalaForm,
                      'sucursala': sucursala,
                  })


def editAngajat(request, id):
    banca = get_object_or_404(Angajati, id=id)
    if request.method == 'POST':
        angajatForm = AngajatForm(request.POST, instance=banca)
        if angajatForm.is_valid():
            angajatForm.save()
            return redirect('/angajati')
    else:
        angajatForm = AngajatForm(instance=banca)

    angajatForm = AngajatForm()
    return render(request, 'editareAngajat.html',
                  {
                      'angajatForm': angajatForm,
                      'banca': banca,
                  })


def deleteBanca(request, id):
    banca = get_object_or_404(Banci, id=id)
    if request.method == 'POST':
        deleteForm = BancaDeleteForm(request.POST, instance=banca)
        if deleteForm.is_valid():
            banca.delete()
            return redirect('/banci')
    else:
        deleteForm = BancaDeleteForm(instance=banca)

    deleteForm = BancaDeleteForm()
    return render(request, 'banci.html',
                  {
                      'form': deleteForm,
                      'banca': banca,
                  })


def deleteSucursala(request, id):
    sucursala = get_object_or_404(Sucursale, id=id)
    if request.method == 'POST':
        deleteForm = SucursalaDeleteForm(request.POST, instance=sucursala)
        if deleteForm.is_valid():
            sucursala.delete()
            return redirect('/sucursale')
    else:
        deleteForm = SucursalaDeleteForm(instance=sucursala)

    deleteForm = SucursalaDeleteForm()
    return render(request, 'sucursale.html',
                  {
                      'form': deleteForm,
                      'sucursala': sucursala,
                  })


def deleteAngajat(request, id):
    angajat = get_object_or_404(Angajati, id=id)
    if request.method == 'POST':
        deleteForm = AngajatDeleteForm(request.POST, instance=angajat)
        if deleteForm.is_valid():
            angajat.delete()
            return redirect('/angajati')
    else:
        deleteForm = AngajatDeleteForm(instance=angajat)

    deleteForm = AngajatDeleteForm()
    return render(request, 'sucursale.html',
                  {
                      'form': deleteForm,
                      'angajat': angajat,
                  })
