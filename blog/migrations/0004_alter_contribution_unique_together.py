# Generated by Django 3.2 on 2021-04-19 14:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_contribution_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contribution',
            unique_together={('user', 'post', 'contribution')},
        ),
    ]
