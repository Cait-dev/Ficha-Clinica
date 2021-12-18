# Generated by Django 2.2.24 on 2021-12-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0016_auto_20211207_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de registro'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='Presion_Intracraneal',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Presion Intracraneal'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='Presion_arterial_pulmonar',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Presion Arterial Pulmonar'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='dolor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dolor'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='evaluacion',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Evaluacion'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha registro'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='frecuencia_cardiaca',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Frecuencia Cardiaca'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='gases',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Gases'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='miccion',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Miccion'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='observaciones',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='peso',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='presion_arterial_media',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Presión Arterial Media'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='presion_venosa_central',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Presión Venosa Central'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='respiracion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Respiracion'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='saturacion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Saturacion'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='talla',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Talla'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='temperatura',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='tension',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tension'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='transfusion_sangre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Transfusion de Sangre'),
        ),
        migrations.AlterField(
            model_name='signosvitales',
            name='vomito',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Vomito'),
        ),
    ]