# Generated by Django 2.1.3 on 2018-12-06 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_is_english'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('page', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]