# Generated by Django 3.2.8 on 2021-10-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]