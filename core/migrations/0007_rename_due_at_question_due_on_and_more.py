# Generated by Django 4.1.6 on 2023-02-09 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_answer_question_id_remove_answer_unit_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='due_at',
            new_name='due_on',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='open_at',
            new_name='opens_on',
        ),
        migrations.AlterField(
            model_name='answer',
            name='time_spent',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('Test', 'Test'), ('Experiment', 'Experiment')], max_length=64),
        ),
        migrations.CreateModel(
            name='PeerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=16384)),
                ('submitted_on', models.DateField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peer_reviews', to='core.unit')),
            ],
        ),
    ]