# Generated by Django 3.1.2 on 2020-10-11 00:11

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('session_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('RUNNING', 'RUNNING'), ('BUILDING', 'BUILDING')], default='COMPLETE', max_length=10)),
                ('test_profile_id', models.CharField(max_length=200)),
                ('time_started', models.DateTimeField()),
                ('time_resolved', models.DateTimeField(null=True)),
                ('time_expired', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_read', models.DateTimeField(null=True)),
                ('raw_captured_image_file_path', models.CharField(max_length=200, null=True)),
                ('results', jsonfield.fields.JSONField(default=dict)),
                ('classifier_results', jsonfield.fields.JSONField(default=dict)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdt.testsession')),
            ],
        ),
    ]
