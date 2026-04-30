from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ct/', views.Create_task),
    path('delete/<int:id>/', views.delete_task, name='delete'),
    path('edit/<int:id>/', views.edit_task, name='ed'),
    path('ver/<int:id>/', views.ver, name='ver_'),
    path('ver/<int:id>/pdf/', views.descargar_nota_pdf, name='descargar_nota_pdf'),
    path('sp/', views.SinPrevio),
    path('grabado/', views.EnGrabado),
    path('entregar/', views.Entregar),
]