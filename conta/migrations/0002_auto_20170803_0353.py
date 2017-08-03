# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saque',
            old_name='quantidade_notas',
            new_name='valor',
        ),
        migrations.RemoveField(
            model_name='saque',
            name='caixa',
        ),
        migrations.AlterField(
            model_name='saque',
            name='conta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='conta_saque', serialize=False, to='conta.Conta', verbose_name='id_conta'),
        ),
    ]
