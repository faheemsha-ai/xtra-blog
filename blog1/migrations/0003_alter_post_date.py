# Generated by Django 5.1 on 2024-08-21 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]