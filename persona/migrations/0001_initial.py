# Generated by Django 5.1 on 2024-09-16 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
