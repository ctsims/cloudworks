# Generated by Django 3.1.2 on 2020-10-23 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('domain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='domain.domain', verbose_name='Domain')),
            ],
        ),
        migrations.CreateModel(
            name='TokenProxy',
            fields=[
            ],
            options={
                'verbose_name': 'token',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('domain.token',),
        ),
    ]
