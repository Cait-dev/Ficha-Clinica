# Generated by Django 2.2.24 on 2021-11-21 02:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarAtencion',
            fields=[
                ('idLugarAtencion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20, verbose_name='Lugar de atencion')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombres del Médico')),
                ('snombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo Nombre del Médico')),
                ('apellido', models.CharField(max_length=45, verbose_name='Apellido del Médico')),
                ('sapellido', models.CharField(blank=True, max_length=45, null=True, verbose_name='Segundo Apellido del Médico')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion del Médico')),
                ('especialidad', models.CharField(max_length=200, verbose_name='Especialidad del Médico')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Fecha actualizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('idregistro', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero de registro')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')),
                ('tipoAtencion', models.CharField(max_length=200, verbose_name='Tipo de Atencion')),
                ('Servicio', models.CharField(max_length=200, verbose_name='Servicio')),
                ('Diagnostico', models.CharField(max_length=200, verbose_name='Diagnostico')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=30, verbose_name='Nombres del paciente')),
                ('Apellidos', models.CharField(max_length=45, verbose_name='Apellidos del paciente')),
                ('Direccion', models.CharField(max_length=200, verbose_name='Direccion del paciente')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso')),
                ('n_historial', models.IntegerField(verbose_name='Numero historial')),
                ('lugarAtencion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.LugarAtencion')),
                ('nombreMedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Medico', verbose_name='Nombre Médico')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('idhistorial', models.AutoField(primary_key=True, serialize=False, verbose_name='Id historial')),
                ('idregistro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Registro')),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
        ),
    ]
