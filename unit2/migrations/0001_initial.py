# Generated by Django 2.1.7 on 2019-03-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('random_word', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
