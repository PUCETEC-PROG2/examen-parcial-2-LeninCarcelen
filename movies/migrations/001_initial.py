
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=1)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('T', 'Terror'), ('E', 'Explisito'), ('A', 'Accion'), ('U', 'Urbana'), ('D', 'Documental'), ('F', 'Familiar')], max_length=30)),
                ('director', models.DecimalField(decimal_places=4, max_digits=6)),
                ('hyear', models.DecimalField(decimal_places=4, max_digits=6)),
                ('picture', models.ImageField(upload_to='pokemon_images')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.user')),
            ],
        ),
    ]