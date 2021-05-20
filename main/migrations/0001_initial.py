# Generated by Django 3.2.2 on 2021-05-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('subject', models.CharField(max_length=150, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]