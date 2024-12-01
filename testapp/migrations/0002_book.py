# Generated by Django 4.0 on 2024-11-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publication', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField()),
            ],
        ),
    ]
