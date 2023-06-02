# Generated by Django 4.2.1 on 2023-06-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_operational', models.BooleanField(default=True)),
                ('is_door_open', models.BooleanField(default=False)),
                ('current_floor', models.PositiveIntegerField(default=1)),
                ('direction', models.CharField(choices=[('UP', 'Up'), ('DOWN', 'Down'), ('STOPPED', 'Stopped')], default='STOPPED', max_length=10)),
            ],
        ),
    ]
