# Generated by Django 4.1.6 on 2023-02-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_peerreview_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]
