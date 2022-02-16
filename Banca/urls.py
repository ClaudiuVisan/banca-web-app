from django.urls import path
from Banca import views


urlpatterns = [
    path('', views.index, name='index'),
    path('banci/', views.viewBanci, name='banci'),
    path('sucursale/', views.viewSucursale, name='sucursale'),
    path('angajati/', views.viewAngajati, name='angajati'),
    path('banci/adauga-banca/', views.addBanca, name='adaugareBanca'),
    path('sucursale/adauga-sucursala/', views.addSucursala,
         name='adaugareSucursala'),
    path('angajati/adauga-angajat/', views.addAngajat, name='adaugareAngajat'),
    path('banci/editare-banca/<int:id>', views.editBanca,
         name='editareBanca'),
    path('sucursale/editare-sucursala/<int:id>', views.editSucursala,
         name='editareSucursala'),
    path('angajati/editare-angajat/<int:id>', views.editAngajat,
         name='editareAngajat'),
    path('banci/stergere-banca/<int:id>', views.deleteBanca,
         name='stergereBanca'),
    path('sucursale/stergere-sucursala/<int:id>', views.deleteSucursala,
         name='stergereSucursala'),
    path('banci/stergere-angajat/<int:id>', views.deleteAngajat,
         name='stergereAngajat'),


]
