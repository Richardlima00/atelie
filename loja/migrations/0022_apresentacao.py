# Generated by Django 5.0.6 on 2024-05-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0021_remove_tipo_categoria_categoria_tipos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apresentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('link_destino', models.CharField(blank=True, max_length=400, null=True)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
