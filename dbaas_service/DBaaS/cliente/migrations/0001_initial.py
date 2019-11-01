# Generated by Django 2.2.6 on 2019-10-29 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_Registro', models.DateField()),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
                ('aplausos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('fecha_Registro', models.DateField()),
                ('AreaEspecialidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sintoma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('caracteristicas', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efectividad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_Registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoMedicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Medicamento')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('aplausos', models.IntegerField()),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='ArticuloSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Articulo')),
                ('sintomas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Sintoma')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Doctor'),
        ),
    ]