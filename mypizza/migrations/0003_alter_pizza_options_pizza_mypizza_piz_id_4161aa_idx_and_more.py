# Generated by Django 5.0.4 on 2024-05-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypizza', '0002_alter_pizza_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['title']},
        ),
        migrations.AddIndex(
            model_name='pizza',
            index=models.Index(fields=['id'], name='mypizza_piz_id_4161aa_idx'),
        ),
        migrations.AddIndex(
            model_name='pizza',
            index=models.Index(fields=['title'], name='mypizza_piz_title_8adff5_idx'),
        ),
    ]