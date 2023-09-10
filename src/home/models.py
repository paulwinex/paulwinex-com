from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class GalleryItemPage(Page):
    template = 'home/gallery_item.html'
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('content'),
    ]

    subtitle = models.CharField(max_length=256, blank=True, null=True)
    image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    content = StreamField([
        ('heading', CharBlock(classname="full title", icon="title")),
        ('text', RichTextBlock(icon="text")),
        ('image', ImageChooserBlock()),
    ], blank=True, null=True, use_json_field=True)


class GalleryPage(Page):
    template = 'home/gallery.html'
    parent_page_type = []
    subpage_types = [GalleryItemPage]
    max_count = 1
