# Generated by Django 2.2.2 on 2019-06-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mesage',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
