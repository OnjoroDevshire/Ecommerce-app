# Generated by Django 4.1.7 on 2023-09-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('oldPrice', models.FloatField()),
                ('price', models.FloatField()),
                ('isNew', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('ratings', models.FloatField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]