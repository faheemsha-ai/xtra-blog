# Generated by Django 5.1 on 2024-08-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0003_alter_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]