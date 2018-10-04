# Generated by Django 2.1.2 on 2018-10-04 19:18

from django.db import migrations

def create_default_images(apps, schema_editor):
    Image = apps.get_model('images', 'Image')
    Image.objects.create(
        name='default',
        value='default.jpeg'
    )
class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_default_images,
            lambda x, y: (x, y)
        )
    ]
