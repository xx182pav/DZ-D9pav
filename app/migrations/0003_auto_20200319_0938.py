# Generated by Django 2.2.6 on 2020-03-19 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200318_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='app.Post'),
        ),
    ]
