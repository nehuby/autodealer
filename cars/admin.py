from django.contrib import admin

from .models import Brand, CallBack, Car, Photo, Review


class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin[Car]):
    inlines = [PhotoAdmin]
    list_display = (
        "id",
        "car_brand",
        "car_model",
        "body_type",
        "equipment_name",
        "price",
    )
    list_filter = ("car_brand", "body_type", "year", "equipment_name")
    search_fields = ("car_brand", "car_model")

    class Meta:
        model = Car


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin[Brand]):
    list_display = ("id", "name")


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin[CallBack]):
    list_display = ("id", "full_name", "phone")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin[Review]):
    list_display = ("id", "username", "rating")
