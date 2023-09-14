from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.blocks import CharBlock, RichTextBlock, BlockQuoteBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


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
        ('heading', CharBlock(icon="title")),
        ('text', RichTextBlock(icon="text")),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True, null=True, use_json_field=True)


class ResumePage(Page):
    template = 'home/resume.html'
    # parent_page_type = []
    subpage_types = []
    max_count = 1

    content = StreamField([
        # ('heading', CharBlock(icon="title")),
        ('text', RichTextBlock(icon="title")),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock(max_width=800, max_height=400)),
        ('quote', BlockQuoteBlock(icon='openquote'))
    ], blank=True, null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]


class GalleryPage(Page):
    template = 'home/gallery.html'
    parent_page_type = []
    subpage_types = [GalleryItemPage, ResumePage]
    max_count = 1

