# Generated by Django 2.0.7 on 2018-08-12 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(null=True)),
                ('developer', models.CharField(max_length=100)),
                ('published_by', models.CharField(max_length=100)),
                ('image', models.ImageField(default='images/placeholder.png', upload_to='images/')),
                ('highlighted', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-highlighted', 'name'],
            },
        ),
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gameplatform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.GamePlatform'),
        ),
    ]
