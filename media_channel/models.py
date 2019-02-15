from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

class Channel(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=50),
    language = models.CharField(verbose_name=_('Language'), max_length=5, default='US-en')
    picture = models.ImageField(verbose_name=_('Picture'),null=True)
    parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class HeadGroup(models.Model):
    ACTIVE = 'a'
    PASSIVE = 'p'
    STATUS_CHOICE = (
        (ACTIVE, _('Active')),
        (PASSIVE, _('Passive'))
    )
    title = models.CharField(verbose_name=_('Title'), max_length=50),
    status = models.CharField(verbose_name=_('Status'), max_length=1, choices=STATUS_CHOICE, default=ACTIVE)

    def __str__(self):
        return self.title

class ChannelGroup(models.Model):
    group = models.ForeignKey(HeadGroup, verbose_name=_('Group'), on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, verbose_name=_('channel'), on_delete=models.CASCADE)

    @property
    def name(self):
        return "%s".format(str(self.group))

    def __str__(self):
        return self.name

class Content(models.Model):
    channel = models.ForeignKey(Channel, verbose_name=_('channel'), on_delete=models.CASCADE)
    file = models.FileField(verbose_name=_('Upload File'))
    meta_data = models.CharField(verbose_name=_('Meta data'), max_length=100, blank=True)
    rating_no = models.PositiveSmallIntegerField(verbose_name=_('Rate'), default=0,
                                                 validators=[MinValueValidator(0), MaxValueValidator(10)])



