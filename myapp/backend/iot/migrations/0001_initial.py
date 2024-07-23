# Generated by Django 4.2.6 on 2024-05-23 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyEnergySum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_energy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('end_of_day', models.DateTimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HourlyEnergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(unique=True)),
                ('energy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('inverterID', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('serialNumber', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyEnergySum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_energy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('end_of_month', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PowerMeterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_id', models.CharField(max_length=10, null=True)),
                ('timestamp', models.DateTimeField()),
                ('power', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('voltage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('current', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('energy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('siteID', models.AutoField(primary_key=True, serialize=False)),
                ('siteName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SiteMeasurements',
            fields=[
                ('siteMeasurementID', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('irradiation', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('m_yield', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('irradiance', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('production', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('powerratio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('activepower', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.site')),
            ],
        ),
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
        migrations.CreateModel(
            name='InverterMeasurement',
            fields=[
                ('measurementID', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('meterReadTotalEnergy', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('activePower', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inputPower', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('efficiency', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('internalTemp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('gridFrequency', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('productionToday', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('yieldToday', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('reactivePower', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('apparentPower', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('powerFactor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stage', models.CharField(blank=True, max_length=20, null=True)),
                ('inverter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.inverter')),
            ],
        ),
        migrations.AddField(
            model_name='inverter',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.site'),
        ),
    ]