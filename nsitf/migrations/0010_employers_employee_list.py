# Generated by Django 2.0.13 on 2019-12-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsitf', '0009_reg_task_queue_reg_task_route_reg_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='employers',
            name='employee_list',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
