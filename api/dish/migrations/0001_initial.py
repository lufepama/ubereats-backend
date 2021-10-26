# Generated by Django 3.1.7 on 2021-10-22 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('previous_price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
