# Generated by Django 2.0.13 on 2019-12-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsitf', '0010_employers_employee_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
    ]