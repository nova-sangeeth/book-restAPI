# Generated by Django 3.0.5 on 2020-04-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_book_store_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_store',
            name='publication',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
