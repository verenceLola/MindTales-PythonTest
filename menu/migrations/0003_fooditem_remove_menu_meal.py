# Generated by Django 4.0.6 on 2022-07-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_alter_restaurant_table_restaurant_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('meal', models.CharField(choices=[('BF', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='L', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='meal',
        ),
    ]
