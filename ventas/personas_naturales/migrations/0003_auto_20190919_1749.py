# Generated by Django 2.2.5 on 2019-09-19 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas_naturales', '0002_auto_20190919_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona_natural',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Cédula'),
        ),
    ]