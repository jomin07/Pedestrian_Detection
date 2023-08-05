# Generated by Django 3.2.16 on 2023-04-07 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imagess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=150)),
                ('image', models.FileField(max_length=200, upload_to='')),
                ('result', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='registerr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]