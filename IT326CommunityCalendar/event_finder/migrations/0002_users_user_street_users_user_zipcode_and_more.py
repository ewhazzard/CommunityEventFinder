# Generated by Django 4.1.3 on 2022-12-04 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_street',
            field=models.CharField(default='placeholder', max_length=100, verbose_name='Location: Street'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_zipcode',
            field=models.IntegerField(default=0, verbose_name='Location: Zipcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_finder.users', verbose_name='OrganizerID'),
        ),
    ]