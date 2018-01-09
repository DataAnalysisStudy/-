# Generated by Django 2.0 on 2018-01-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KrongKrongCrawl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CauData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='BlogData',
            new_name='BisData',
        ),
    ]
