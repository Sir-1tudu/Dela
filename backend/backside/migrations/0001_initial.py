# Generated by Django 4.2.4 on 2023-09-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@gamil.com', max_length=254)),
                ('dateAndTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]