# Generated by Django 3.2.12 on 2022-04-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportcompetition', '0003_alter_schueler_schnr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schueler',
            name='id',
        ),
        migrations.AlterField(
            model_name='schueler',
            name='schnr',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
