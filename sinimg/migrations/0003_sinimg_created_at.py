# Generated by Django 3.2.15 on 2022-10-23 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sinimg', '0002_alter_sinimg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinimg',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]