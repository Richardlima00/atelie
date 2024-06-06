# Generated by Django 5.0.6 on 2024-05-27 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0011_remove_tipo_categoria_categoria_tipos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='tipos',
        ),
        migrations.AddField(
            model_name='tipo',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tipos', to='loja.categoria'),
        ),
    ]
