# Generated by Django 2.1.2 on 2019-12-12 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('adopter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
