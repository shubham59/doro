# Generated by Django 2.1.2 on 2019-12-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]