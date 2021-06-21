# Generated by Django 2.2.22 on 2021-06-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostResourcingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('rates', models.TextField()),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cost_resourcing_model',
                'ordering': ['name'],
            },
        ),
        migrations.AddIndex(
            model_name='costresourcingmodel',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='costresourcingmodel',
            index=models.Index(fields=['updated_timestamp'], name='updated_timestamp_idx'),
        ),
    ]
