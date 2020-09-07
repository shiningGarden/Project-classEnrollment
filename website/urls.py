from django.contrib import admin
from django.urls import path
import web.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web.views.home, name='home'),
    path('board/', web.views.board, name='board'),
    path('detail/<int:id>', web.views.detail, name='detail'),
    path('ratings/<int:id>', web.views.ratings, name='ratings'),
    path('login/', web.views.login, name='login'),
    path('signup/', web.views.signup, name='signup'),
    path('rate/', web.views.rate, name='rate'),
    path('lecture/', web.views.lecture, name = 'lecture'),
    path('new/', web.views.new, name='new'),
    path('update/<int:id>', web.views.update, name='update'),
    path('delete/<int:id>', web.views.delete, name='delete'),
    path('new/create', web.views.create, name='create'),
    path('logout', web.views.logout, name='logout'),
    
]
