# Generated by Django 5.1.4 on 2025-01-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_marketplaceitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceitem',
            name='image_review',
            field=models.ImageField(blank=True, null=True, upload_to='images/reviews/'),
        ),
    ]
