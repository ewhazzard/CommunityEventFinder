# Generated by Django 4.1.3 on 2022-12-05 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_finder', '0002_users_user_street_users_user_zipcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_string',
            field=models.TextField(default='NULL', verbose_name='Comment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_finder.users', verbose_name='User ID'),
        ),
    ]