from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_remove_ad_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]