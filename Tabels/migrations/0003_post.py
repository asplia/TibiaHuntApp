# Generated by Django 2.1.1 on 2018-10-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tabels', '0002_auto_20181027_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=500)),
            ],
        ),
    ]
