from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('new', views.new),
  path('create', views.create),
  path('<int:show_id>', views.show, name="show"),
  path('<int:show_id>/edit', views.edit, name="edit"),
  path('<int:show_id>/update', views.update, name="update"),
  path('<int:show_id>/delete', views.delete, name="delete")
]