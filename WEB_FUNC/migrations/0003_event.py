# Generated by Django 2.0.2 on 2018-03-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEB_FUNC', '0002_auto_20180223_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1)),
            ],
        ),
    ]
