from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

    path('', views.TasksList.as_view(), name='tasks'),
    path('create', views.TaskCreate.as_view(), name='create'), 
    path('update/<int:pk>', views.UpdateTask.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete'),
]
