"""
URL configuration for day1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from task2.views import *

urlpatterns = [
    
    #^ Home
    path('',home),
    path('home/',home,name='home'),
    path('aboutus/',about,name='aboutus'),    
    
    #^ Products
    path('products/',products,name='products'),
    path('productDetails/<int:id>/',productDetails,name='productDetails'),
    path('addProduct/',addProduct,name='addProduct'),
    path('deleteProduct/<int:id>/',deleteProduct,name='deleteProduct'),
    path('updateProduct/<int:id>/',updateProduct,name='updateProduct'),
    
    #^ Categories
    path('categories/',categories,name='categories'),
    path('addCategory/',addCategory,name='addCategory'),
    path('deleteCategory/<int:id>/',deleteCategory,name='deleteCategory'),
    path('updateCategory/<int:id>/',updateCategory,name='updateCategory'),
    
    #^ Tracks
    path('tracks/',alltracks,name='tracks'),
    path('mytrack/<int:id>/',mytrack,name='mytrack'),
    path('aboutus/',about,name='aboutus'),
]
