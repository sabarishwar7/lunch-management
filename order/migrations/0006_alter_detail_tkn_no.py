# Generated by Django 4.2.3 on 2023-08-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_dish_rename_category_menu_cate_remove_menu_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='tkn_no',
            field=models.CharField(default='T<django.db.models.query_utils.DeferredAttribute object at 0x000001B90DB802E0>', max_length=6),
        ),
    ]
