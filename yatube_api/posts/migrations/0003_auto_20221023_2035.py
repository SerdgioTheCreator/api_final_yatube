# Generated by Django 2.2.16 on 2022-10-23 20:35

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20221021_1553'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='already_follow',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='self_subscription',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='already_follow'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='self_subscription'),
        ),
    ]