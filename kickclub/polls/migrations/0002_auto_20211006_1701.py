# Generated by Django 3.2.8 on 2021-10-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='id_custumer',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='custumer',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]