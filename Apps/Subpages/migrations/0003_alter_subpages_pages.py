# Generated by Django 4.1.1 on 2022-09-11 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
        ('Subpages', '0002_rename_pages_id_subpages_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subpages',
            name='pages',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Pages.pages'),
        ),
    ]
