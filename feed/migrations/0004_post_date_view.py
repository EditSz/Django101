from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_view',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        )
    ]