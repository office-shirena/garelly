# Generated by Django 2.2.5 on 2020-05-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=5)),
                ('companyName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keycompanyCode', models.CharField(max_length=5)),
                ('keycompanyName', models.CharField(max_length=100)),
                ('relatedcompanyCode', models.CharField(max_length=5)),
                ('relatedcompanyName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=5)),
                ('userEmail', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=5)),
                ('picture', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendDate', models.DateTimeField(auto_now_add=True)),
                ('sndCompanycode', models.CharField(max_length=5)),
                ('sndCompanyname', models.CharField(max_length=100)),
                ('rcvCompanycode', models.CharField(max_length=5)),
                ('rcvCompanyname', models.CharField(max_length=100)),
                ('messagetext', models.TextField(max_length=300)),
                ('updateUser', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pallets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyid', models.CharField(max_length=10)),
                ('PLtype', models.CharField(max_length=1)),
                ('PLname', models.CharField(max_length=100)),
                ('PLvolume', models.CharField(max_length=5)),
                ('sndCompanycode', models.CharField(max_length=5)),
                ('sndCompanyName', models.CharField(max_length=100, null=True)),
                ('rcvCompanycode', models.CharField(max_length=5)),
                ('rcvCompanyName', models.CharField(max_length=100, null=True)),
                ('sndDate', models.DateField()),
                ('rcvDate', models.DateField()),
                ('updateUser', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pallettype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PLtype', models.CharField(max_length=1)),
                ('PLname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SendPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planNo', models.CharField(max_length=10)),
                ('sndPlanDate', models.DateField()),
                ('rcvPlanDate', models.DateField()),
                ('PLtype', models.CharField(max_length=1)),
                ('PLname', models.CharField(max_length=100)),
                ('PLvolume', models.CharField(max_length=5)),
                ('sndCompanycode', models.CharField(max_length=5)),
                ('sndCompanyName', models.CharField(max_length=100, null=True)),
                ('rcvCompanycode', models.CharField(max_length=5)),
                ('rcvCompanyName', models.CharField(max_length=100, null=True)),
                ('rcvFlg', models.BooleanField()),
                ('updateUser', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=5)),
                ('companyName', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, null=True)),
                ('picture', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ZaikoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=5)),
                ('companyName', models.CharField(max_length=100)),
                ('JidoTagPL', models.CharField(max_length=5)),
                ('NonTagPL', models.CharField(max_length=5)),
            ],
        ),
    ]
