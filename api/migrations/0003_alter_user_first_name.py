# Generated by Django 5.0.6 on 2024-06-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
    ]
