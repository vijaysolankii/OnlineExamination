# Generated by Django 2.1.1 on 2019-01-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190110_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_of_profile',
            field=models.CharField(choices=[('AD', 'Admin'), ('TE', 'Teacher'), ('SU', 'Student')], default='SU', max_length=2),
        ),
    ]
