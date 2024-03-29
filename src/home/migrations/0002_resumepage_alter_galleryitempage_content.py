# Generated by Django 4.2.5 on 2023-09-14 07:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('content', wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(icon='title')), ('text', wagtail.blocks.RichTextBlock(icon='text')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800)), ('quote', wagtail.blocks.BlockQuoteBlock(icon='openquote'))], blank=True, null=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='galleryitempage',
            name='content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(icon='title')), ('text', wagtail.blocks.RichTextBlock(icon='text')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(max_height=400, max_width=800))], blank=True, null=True, use_json_field=True),
        ),
    ]
