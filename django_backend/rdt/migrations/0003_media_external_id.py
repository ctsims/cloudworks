# Generated by Django 3.1.2 on 2020-10-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdt', '0002_auto_20201026_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='external_id',
            field=models.CharField(default=22, max_length=255),
            preserve_default=False,
        ),
    ]