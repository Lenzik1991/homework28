from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_location_alter_category_options_ad_category_ad_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
    ]