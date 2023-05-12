from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from cars import forms, models


class IndexRedirectView(RedirectView):
    url = "cars"


class CarListView(ListView):
    model = models.Car
    template_name = "cars/cars.html"

    def get_queryset(self) -> QuerySet[models.Car]:
        return super().get_queryset().filter(amount__gt=0)


class CarDetailView(DetailView):
    model = models.Car
    template_name = "cars/car_detail.html"


class BrandListView(ListView):
    model = models.Brand
    template_name = "cars/brands.html"


class CallBackCreateView(CreateView):
    form_class = forms.CallBackForm
    template_name = "cars/callback.html"
    success_url = "/callback/"

    def form_valid(self, form):
        messages.success(self.request, _("Callback has been left, expect a call"))
        return super().form_valid(form)


class ReviewListCreateView(CreateView, ListView):
    model = models.Review
    paginate_by = 3
    form_class = forms.ReviewForm
    template_name = "cars/reviews.html"
    success_url = "/reviews/"

    def form_valid(self, form):
        messages.success(self.request, _("You left a new review"))
        return super().form_valid(form)


def reviews(request: HttpRequest) -> HttpResponse:
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ReviewForm()
    paginator = Paginator(models.Review.objects.all().order_by("-rating"), 3)
    try:
        page_number = int(request.GET["page"])
    except (KeyError, ValueError):
        page_number = 1
    else:
        if page_number < 1:
            page_number = 1
        elif page_number > paginator.num_pages:
            page_number = paginator.num_pages
    reviews = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(
        number=page_number, on_each_side=1, on_ends=1
    )
    context = {
        "form": form,
        "reviews": reviews,
        "page_range": page_range,
    }
    return render(request, "cars/reviews.html", context)


class ContactTemplateView(TemplateView):
    template_name = "cars/contacts.html"
