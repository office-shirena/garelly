# Generated by Django 2.2.5 on 2020-05-14 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pallets',
            name='rcvCompanyName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pallets',
            name='sndCompanyName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sendplan',
            name='rcvCompanyName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sendplan',
            name='sndCompanyName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]