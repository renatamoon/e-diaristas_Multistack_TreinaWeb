# Generated by Django 3.2.9 on 2021-12-09 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor_minimo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('qtd_horas', models.IntegerField()),
                ('porcentagem_comissao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_quarto', models.IntegerField()),
                ('valor_quarto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_sala', models.IntegerField()),
                ('valor_sala', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_banheiro', models.IntegerField()),
                ('valor_banheiro', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_cozinha', models.IntegerField()),
                ('valor_cozinha', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_quintal', models.IntegerField()),
                ('valor_quintal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('horas_outros', models.IntegerField()),
                ('valor_outros', models.DecimalField(decimal_places=2, max_digits=5)),
                ('icone', models.CharField(choices=[('twf-cleaning-1', 'twf-cleaning-1'), ('twf-cleaning-2', 'twf-cleaning-2'), ('twf-cleaning-3', 'twf-cleaning-3')], max_length=14)),
                ('posicao', models.IntegerField()),
            ],
        ),
    ]
