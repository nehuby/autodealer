from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Brand(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100, unique=True)
    logo = models.ImageField(verbose_name=_("logo"), upload_to="logo/")
    country = CountryField(verbose_name=_("country"))

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.name


class Car(models.Model):
    class BodyTypes(models.TextChoices):
        SEDAN = "SEDAN", _("Sedan")
        LIMOUSINE = "LIMOUSINE", _("Limousine")
        HATCHBACK = "HATCHBACK", _("Hatchback")
        LIFTBACK = "LIFTBACK", _("Liftback")
        STATION_WAGON = "SW", _("Station wagon")
        COUPE = "COUPE", _("Coupe")
        CONVERTIBLE = "CONVERTIBLE", _("CONVERTIBLE")
        ROADSTER = "ROADSTER", _("Roadster")
        TARGA = "TARGA", _("Targa")
        MINIVAN = "MINIVAN", _("Minivan")
        PICKUP = "PICKUP", _("Pickup")
        CROSSOVER = "CROSSOVER", _("Crossover")
        COUPE_CROSSOVER = "CCROSSOVER", _("Coupe-crossover")
        COUPE_CONVERTIBLE = "CCONVERTIBLE", _("Coupe-cabriolet")
        SPEEDSTER = "SPEEDSTER", _("Speedster")
        SUV = "SUV", _("SUV")

    class Transmissions(models.TextChoices):
        AUTOMATIC = "AT", _("Automatic")
        MANUAL = "MT", _("Manual")
        SEMI_AUTOMATIC = "SAT", _("Semi-automatic")

    class DriveUnits(models.TextChoices):
        FRONT_WHEEL = "FWD", _("Front wheel drive")
        REAR_WHEEL = "RWD", _("Rear wheel drive")
        FOUR_WHEEL = "4WD", _("Four wheel drive")

    class EngineTypes(models.TextChoices):
        GASOLINE = "G", "Gasoline"
        DIESEL = "D", "Diesel"
        HYBRID = "H", "Hybrid"
        ELECTRIC = "E", "Electric"

    car_brand = models.ForeignKey(
        Brand, verbose_name=_("car brand"), on_delete=models.CASCADE
    )
    car_model = models.CharField(verbose_name=_("car model"), max_length=100)
    body_type = models.CharField(
        verbose_name=_("body type"), max_length=50, choices=BodyTypes.choices
    )
    year = models.PositiveIntegerField(verbose_name=_("year of issue"))
    equipment_name = models.CharField(verbose_name=_("equipment name"), max_length=100)
    equipment_description = models.TextField(
        verbose_name=_("equipment description"), blank=True
    )
    transmission = models.CharField(
        verbose_name=_("transmission"), max_length=50, choices=Transmissions.choices
    )
    number_of_gears = models.PositiveSmallIntegerField(
        verbose_name=_("number of gears"),
        validators=(MinValueValidator(4), MaxValueValidator(12)),
    )
    drive_unit = models.CharField(
        verbose_name=_("drive unit"), max_length=50, choices=DriveUnits.choices
    )
    engine_type = models.CharField(
        verbose_name=_("engine's type"), max_length=50, choices=EngineTypes.choices
    )
    working_volume = models.PositiveSmallIntegerField(verbose_name=_("working volume"))
    engine_power = models.PositiveSmallIntegerField(verbose_name=_("engine power"))
    price = models.PositiveIntegerField(verbose_name=_("price"))
    amount = models.PositiveSmallIntegerField(_("amount"))

    class Meta:
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.car_brand} {self.car_model}"


class Photo(models.Model):
    photo = models.ImageField(verbose_name=_("photo"), upload_to="photo/")
    car = models.ForeignKey(Car, verbose_name=_("car"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("photo")
        verbose_name_plural = _("photos")


class CallBack(models.Model):
    full_name = models.CharField(verbose_name=_("full name"), max_length=254)
    phone = PhoneNumberField(verbose_name=_("phone"), region="RU")
    comment = models.TextField(verbose_name=_("comments"), blank=True)

    class Meta:
        verbose_name = _("callback")
        verbose_name_plural = _("callbacks")

    def __str__(self):
        return f"{self.full_name}: {self.phone}"


class Review(models.Model):
    RATING = tuple((i, str(i)) for i in range(1, 6))
    username = models.CharField(verbose_name=_("username"), max_length=100)
    rating = models.PositiveSmallIntegerField(_("rating"), choices=RATING)
    text = models.TextField(verbose_name=_("text"))

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return self.username

    def review_len(self):
        return len(self.text)
