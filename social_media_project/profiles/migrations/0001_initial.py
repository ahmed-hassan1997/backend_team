# Generated by Django 3.0.5 on 2020-05-10 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('idprofiles', models.AutoField(primary_key=True, serialize=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('career', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'profiles',
                'managed': False,
            },
        ),
    ]
