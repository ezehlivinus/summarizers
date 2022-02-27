


from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', views.DataModelView, basename='summaries')
# urlpatterns = router.urls

urlpatterns = [
  path('', views.DataModelView.as_view({'get': 'list', 'post': 'create'}), name='summaries'),
  path('<int:pk>/', views.DataModelView.as_view({'get': 'retrieve'}), name='summaries'),
  # path('data/', views.list, name='list data')
   
  # path('products/<int:id>/', views.product_detail, name='product_detail'),
]
