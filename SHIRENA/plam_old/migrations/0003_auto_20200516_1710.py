# Generated by Django 2.2.5 on 2020-05-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plam', '0002_auto_20200514_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='updateUser',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pallets',
            name='updateUser',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sendplan',
            name='updateUser',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
