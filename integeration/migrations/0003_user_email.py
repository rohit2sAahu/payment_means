# Generated by Django 3.2.4 on 2021-07-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integeration', '0002_user_confirmpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]