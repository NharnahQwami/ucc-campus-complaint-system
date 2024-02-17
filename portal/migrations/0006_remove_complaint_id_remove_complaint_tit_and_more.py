# Generated by Django 4.2.5 on 2023-09-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_complaint_tit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='id',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='tit',
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_id',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
