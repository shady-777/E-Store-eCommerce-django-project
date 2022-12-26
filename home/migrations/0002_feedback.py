# Generated by Django 4.1.4 on 2022-12-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='media')),
                ('desc', models.TextField()),
            ],
        ),
    ]
