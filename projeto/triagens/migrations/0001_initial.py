# Generated by Django 3.0.4 on 2020-11-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Triagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text=' Campos obrigatórios', max_length=20, unique=True, verbose_name='Código da triagem *')),
                ('data', models.DateField(help_text='dd/mm/aaaa', max_length=11, verbose_name='Data da consulta *')),
                ('hora', models.CharField(help_text='hh:mm', max_length=5, verbose_name='Hora da consulta *')),
                ('nomePaciente', models.CharField(max_length=50, verbose_name='Nome Completo do Paciente *')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('altura', models.FloatField(verbose_name='Altura')),
                ('peso', models.FloatField(verbose_name='Peso')),
                ('IMC', models.FloatField(verbose_name='IMC')),
                ('febre', models.BooleanField(verbose_name='Tem Febre?')),
                ('dorCabeca', models.BooleanField(verbose_name='Tem Dor de Cabeça?')),
                ('secrecaoEspirro', models.BooleanField(verbose_name='Tem Secreção nasal ou espirro?')),
                ('dorGarganta', models.BooleanField(verbose_name='Tem Dor/Irritação na garganta?')),
                ('tosseSeca', models.BooleanField(verbose_name='Tem Tosse Seca?')),
                ('dificuldadeRespiratoria', models.BooleanField(verbose_name='Tem Dificuldade Respiratória?')),
                ('doresCorpo', models.BooleanField(verbose_name='Tem Dores no Corpo?')),
                ('diarreia', models.BooleanField(verbose_name='Tem Diarreia?')),
                ('viagem', models.BooleanField(verbose_name='Viajou, nos últimos 14 dias, para um local com casos confirmados de COVID-19?')),
                ('contato', models.BooleanField(verbose_name='Esteve em contato, nos últimos 14 dias, com um caso diagnosticados com COVID-19?')),
                ('ResultadoTriagem', models.CharField(max_length=5, verbose_name='Resultado')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'triagem',
                'verbose_name_plural': 'triagens',
                'ordering': ['codigo', '-data', '-hora'],
                'unique_together': {('codigo', 'data', 'hora')},
            },
        ),
    ]