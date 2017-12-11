# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(blank=True, upload_to='documents/')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('date_of_joining', models.DateField()),
                ('pan_number', models.CharField(max_length=255)),
                ('bank_account_number', models.CharField(max_length=255)),
                ('emergency_contact_number', models.CharField(max_length=11)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile/')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Project'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, max_length=16, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Role'),
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.ManyToManyField(to='account.Skill'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Employee'),
        ),
    ]
