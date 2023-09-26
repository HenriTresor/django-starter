# Generated by Django 4.2.5 on 2023-09-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=155)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
