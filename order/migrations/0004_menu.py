# Generated by Django 2.2 on 2023-08-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20230804_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('food', 'Food'), ('snack', 'Snack'), ('drink', 'Drink')], default='food', max_length=30)),
            ],
        ),
    ]
