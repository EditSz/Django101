from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]