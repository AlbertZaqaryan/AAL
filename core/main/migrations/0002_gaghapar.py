# Generated by Django 4.0.5 on 2022-06-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gaghapar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Gaghapar name1')),
                ('about', models.TextField(verbose_name='Gaghapar desc')),
                ('img', models.ImageField(upload_to='media', verbose_name='Gaghapar image')),
            ],
            options={
                'verbose_name': 'Gaghapar',
                'verbose_name_plural': 'Gaghapars',
            },
        ),
    ]