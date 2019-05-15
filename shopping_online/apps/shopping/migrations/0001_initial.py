# Generated by Django 2.1.7 on 2019-05-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255, verbose_name='商品名')),
                ('image', models.CharField(max_length=500, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
                ('classify', models.CharField(max_length=100, verbose_name='分类')),
            ],
        ),
    ]