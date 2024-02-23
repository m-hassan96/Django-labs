# Generated by Django 5.0.2 on 2024-02-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=50, null=True)),
                ('image', models.CharField(max_length=100, null=True)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('updatedate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
