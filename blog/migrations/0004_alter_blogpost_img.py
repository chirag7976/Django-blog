# Generated by Django 4.0.3 on 2022-06-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='media/media'),
        ),
    ]