from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexRedirectView.as_view()),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("car/<int:pk>/", views.CarDetailView.as_view(), name="car"),
    path("brands/", views.BrandListView.as_view(), name="brands"),
    path("callback/", views.CallBackCreateView.as_view(), name="callback"),
    path("reviews/", views.reviews, name="reviews"),
    path("contacts/", views.ContactTemplateView.as_view(), name="contacts"),
]
