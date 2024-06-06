# Generated by Django 5.0.6 on 2024-05-27 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0012_remove_categoria_tipos_tipo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipos', to='loja.categoria'),
        ),
    ]
