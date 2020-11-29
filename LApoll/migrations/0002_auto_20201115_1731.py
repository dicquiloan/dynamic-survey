# Generated by Django 3.1.2 on 2020-11-15 17:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LApoll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='response',
        ),
        migrations.AddField(
            model_name='participant',
            name='livesInLA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='participant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='LApoll.participant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='LApoll.question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
