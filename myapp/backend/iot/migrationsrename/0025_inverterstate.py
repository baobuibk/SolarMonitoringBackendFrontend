# Generated by Django 4.2.6 on 2024-05-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0024_delete_inverterstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='InverterState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('starton', models.DateTimeField(null=True)),
                ('inverter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.inverter')),
            ],
        ),
    ]
