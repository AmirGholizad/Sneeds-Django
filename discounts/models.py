import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.
from django.urls import reverse

User = get_user_model()


class Cafe(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=256, blank=False, default="تهران")
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(max_length=128, blank=False, unique=True, default="default")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('discounts:cafe_page', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Discount(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, blank=True, null=True, related_name="discounts")
    discount_percent = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now=True, blank=False)

    def string_represent(self):
        return "تخفیف {}% {}".format(self.discount_percent, self.cafe.name)

    def __str__(self):
        return "{} درصد تخفیف {}".format(self.discount_percent,self.cafe.name )


class CafeImage(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, blank=True, null=True, related_name="images")
    image = models.ImageField(upload_to="website/cafe_images", blank=True, null=True)


class UserDiscount(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=False, null=False,
                                 related_name="user_discounts")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                             related_name="user_discounts")
    code = models.CharField(unique=True, null=False, blank=False, max_length=128, default="")

    date = models.DateField(auto_now=True, blank=False)

    DISCOUNT_STATUS = (
        ('not_used', "استفاده نشده"),
        ('used', "استفاده شده"),
    )

    status = models.CharField(
        max_length=20,
        choices=DISCOUNT_STATUS,
        blank=True,
        default='not_used',
    )

    class Meta:
        unique_together = (("discount", "user"),)

    def __str__(self):
        return str(self.discount)


class CafeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    cafe = models.OneToOneField(Cafe, on_delete=models.CASCADE, related_name="cafe")

    def __str__(self):
        return self.cafe.name


class UserUsedDiscount(models.Model):
    # When discount object is present.
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True,
                                 related_name="user_used_discounts")
    # When cafe object is present.
    cafe = models.ForeignKey(Cafe, on_delete=models.SET_NULL, null=True,
                             related_name="used_discounts")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                             related_name="user_used_discounts")

    date = models.DateField(auto_now=True, blank=False)
    # Is used for user logs.

    archive_string = models.CharField(null=True, max_length=128)
    used_discount_info = models.CharField(null=True, max_length=128)  # Used for indicating "used", "deleted" ...

    def __str__(self):
        return str(self.archive_string)
