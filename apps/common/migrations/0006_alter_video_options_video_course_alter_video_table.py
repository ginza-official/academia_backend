# Generated by Django 4.2.1 on 2023-05-31 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_video_options_remove_video_video_video_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='common.course'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='video',
            table='videos',
        ),
    ]
