# Generated by Django 3.0 on 2019-12-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
    ]
