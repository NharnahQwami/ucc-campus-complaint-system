# Generated by Django 4.2.5 on 2023-09-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='discription',
        ),
        migrations.AddField(
            model_name='complaint',
            name='faculty',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='title',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]
