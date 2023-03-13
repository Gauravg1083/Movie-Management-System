# Generated by Django 4.1.4 on 2023-02-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('courses', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]