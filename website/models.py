import uuid

from django.contrib.admin import ModelAdmin
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Topic(models.Model):
    subject = models.CharField(max_length=120)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=subject)

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.subject]  # post.  use __unicode__ in place of
        k = self.parent

        while k is not None:
            full_path.append(k.subject)
            k = k.parent

        return ' -> '.join(full_path[::-1])


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    post_image = models.ImageField(upload_to="website/post_images", blank=True)
    slug = models.SlugField(default=uuid.uuid1)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_cat_list(self):  # for now ignore this instance method,
        k = self.topic
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]

    def __str__(self):
        return self.title


class BookletField(models.Model):
    """
    For example Civil Eng, Computer Eng, ...
    """
    subject = models.CharField(max_length=120, blank=False, null=True)
    slug = models.SlugField(null=True, help_text="Lower case")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('website:booklets_field', args=[str(self.slug)])

    def __str__(self):
        return self.subject


class BookletTopic(models.Model):
    """
    For example AP, DS, Environment, ...
    """
    field = models.ForeignKey(BookletField,
                              on_delete=models.CASCADE,
                              related_name='topics',
                              blank=False,
                              null=True)
    subject = models.CharField(max_length=120, blank=False, help_text="Booklet topic", verbose_name="عنوان")
    slug = models.SlugField(null=True, help_text="Lower case")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('website:booklets_topic', args=[str(self.field.slug), str(self.slug)])

    def __str__(self):
        temp_str = self.subject + " | " + self.field.subject
        return temp_str


class Booklet(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(null=True, default=None)

    # Booklet writer name
    owner = models.CharField(max_length=200, blank=True, default="ناشناس")
    topic = models.ForeignKey(BookletTopic, on_delete=models.CASCADE, related_name='booklets', null=True, blank=True)
    teacher = models.CharField(max_length=200, blank=True, default="ناشناس")
    number_of_views = models.IntegerField(default=0,
                                          help_text="لطفا مقدار را عوض نکنید ( به جز در مواقع نیاز شدید و باگ)",
                                          verbose_name="تعداد بازدید")
    booklet_content = models.FileField(upload_to="website/booklet_content", blank=False)
    booklet_image = models.ImageField(upload_to="website/booklet_images", blank=False)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('website:booklets', args=[str(self.slug)])

    def __str__(self):
        return self.title


class UserUploadedBooklet(models.Model):
    """
    This model is for the form that user filled and uploaded website.
    This is temporary form and Admin should validate and upload it in Booklet model.
    """

    title = models.CharField(null=False, blank=False, verbose_name="عنوان", max_length=120)
    field = models.CharField(null=False, blank=False, verbose_name="رشته", max_length=120)
    topic = models.CharField(null=False, blank=False, verbose_name="درس", max_length=120)
    writer = models.CharField(null=False, blank=False, verbose_name="نویسنده", max_length=120)

    # Admin should remove this after manipulating.
    booklet_file = models.FileField(upload_to="website/tmp_booklet_content", null=True, blank=True)

    BOOKLET_STATUS = (
        ('seen', "مشاهده شد"),
        ('pending', "در حال انجام"),
        ('finished', "انجام شد"),
        ('canceled', "لغو شد"),
    )

    status = models.CharField(
        max_length=20,
        choices=BOOKLET_STATUS,
        blank=True,
        default='seen',
        help_text='وضعیت دانلود و آپلود جزوه اصلی',
    )

    def __str__(self):
        # changes tuple to dictionary and gets appropriate value
        farsi_status = dict(self.BOOKLET_STATUS).get(self.status)
        return self.title + " => " + farsi_status


class BookletProblemReport(models.Model):
    booklet = models.ForeignKey(Booklet, on_delete=models.CASCADE, related_name='problems')
    text = models.TextField(verbose_name='گذارش خرابی')

    def __str__(self):
        farsi_text = "گذارش خرابی {}".format(self.booklet)
        return farsi_text
