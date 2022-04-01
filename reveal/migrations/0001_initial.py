import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reveal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_attr', models.CharField(max_length=20, verbose_name='Info asked for')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='contenttypes.ContentType')),
                ('enquiring', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='enquiring',
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
