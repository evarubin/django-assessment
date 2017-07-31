# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 04:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import parler.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField(verbose_name='answer')),
            ],
            options={
                'verbose_name_plural': 'answers',
                'verbose_name': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_correct', models.BooleanField(default=False, verbose_name='correct')),
            ],
            options={
                'verbose_name_plural': 'choices',
                'verbose_name': 'choice',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ChoiceTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('value', models.CharField(max_length=512, verbose_name='value')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='assessment.Choice')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'choice Translation',
                'db_table': 'assessment_choice_translation',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_required', models.BooleanField(default=False, verbose_name='required')),
                ('of_type', models.IntegerField(choices=[(1, 'true or false'), (2, 'multiple choice'), (3, 'text')], default=1, verbose_name='type')),
            ],
            options={
                'verbose_name_plural': 'questions',
                'verbose_name': 'question',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('question', models.CharField(max_length=512, verbose_name='question')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='assessment.Question')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'question Translation',
                'db_table': 'assessment_question_translation',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'results',
                'verbose_name': 'result',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_private', models.BooleanField(default=False, verbose_name='private')),
                ('start_date_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='start time')),
                ('end_date_time', models.DateTimeField(blank=True, null=True, verbose_name='end time')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessment_admin_surveys', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('users', models.ManyToManyField(related_name='assessment_user_surveys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'surveys',
                'verbose_name': 'survey',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SurveyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=160, verbose_name='name')),
                ('slug', models.SlugField(max_length=160, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='assessment.Survey')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'survey Translation',
                'db_table': 'assessment_survey_translation',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='survey',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='assessment.Survey', verbose_name='survey'),
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.Survey', verbose_name='survey'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='assessment.Question', verbose_name='question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assessment.Question', verbose_name='question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='result',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='assessment.Result', verbose_name='result'),
        ),
        migrations.AlterUniqueTogether(
            name='surveytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set([('survey', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='questiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='choicetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('result', 'question')]),
        ),
    ]
