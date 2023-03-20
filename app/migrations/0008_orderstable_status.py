# Generated by Django 4.1.7 on 2023-03-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_orderstable_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstable',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Pending'), ('s', 'Shipped'), ('d', 'Delivered')], default='pending', max_length=8, null=True),
        ),
    ]
