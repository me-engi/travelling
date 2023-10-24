# Generated by Django 4.2.6 on 2023-10-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('itinerary', models.TextField()),
                ('days', models.PositiveIntegerField()),
                ('inclusions', models.TextField()),
                ('exclusions', models.TextField()),
            ],
        ),
    ]