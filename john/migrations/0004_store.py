# Generated by Django 3.1.7 on 2021-07-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0003_auto_20210724_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='store/')),
                ('link', models.URLField()),
                ('price', models.IntegerField(max_length=100)),
            ],
        ),
    ]