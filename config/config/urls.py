from django.contrib import admin
from django.urls import path
from to_do_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', views.LCTaskAPI.as_view()),
    path('api/task/<int:pk>/', views.RUDTaskAPI.as_view())
]



