# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TargetClass'
        db.create_table(u'django_relationship_example_targetclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_relationship_example', ['TargetClass'])

        # Adding model 'OneToOneClass'
        db.create_table(u'django_relationship_example_onetooneclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.related.OneToOneField')(related_name='one_to_one', unique=True, to=orm['django_relationship_example.TargetClass'])),
        ))
        db.send_create_signal(u'django_relationship_example', ['OneToOneClass'])

        # Adding model 'ForeignKeyClass'
        db.create_table(u'django_relationship_example_foreignkeyclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='foreignkeys', to=orm['django_relationship_example.TargetClass'])),
        ))
        db.send_create_signal(u'django_relationship_example', ['ForeignKeyClass'])

        # Adding model 'ManyToManyClass'
        db.create_table(u'django_relationship_example_manytomanyclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_relationship_example', ['ManyToManyClass'])

        # Adding M2M table for field target on 'ManyToManyClass'
        m2m_table_name = db.shorten_name(u'django_relationship_example_manytomanyclass_target')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manytomanyclass', models.ForeignKey(orm[u'django_relationship_example.manytomanyclass'], null=False)),
            ('targetclass', models.ForeignKey(orm[u'django_relationship_example.targetclass'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manytomanyclass_id', 'targetclass_id'])


    def backwards(self, orm):
        # Deleting model 'TargetClass'
        db.delete_table(u'django_relationship_example_targetclass')

        # Deleting model 'OneToOneClass'
        db.delete_table(u'django_relationship_example_onetooneclass')

        # Deleting model 'ForeignKeyClass'
        db.delete_table(u'django_relationship_example_foreignkeyclass')

        # Deleting model 'ManyToManyClass'
        db.delete_table(u'django_relationship_example_manytomanyclass')

        # Removing M2M table for field target on 'ManyToManyClass'
        db.delete_table(db.shorten_name(u'django_relationship_example_manytomanyclass_target'))


    models = {
        u'django_relationship_example.foreignkeyclass': {
            'Meta': {'object_name': 'ForeignKeyClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'foreignkeys'", 'to': u"orm['django_relationship_example.TargetClass']"})
        },
        u'django_relationship_example.manytomanyclass': {
            'Meta': {'object_name': 'ManyToManyClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'many_to_many'", 'symmetrical': 'False', 'to': u"orm['django_relationship_example.TargetClass']"})
        },
        u'django_relationship_example.onetooneclass': {
            'Meta': {'object_name': 'OneToOneClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'one_to_one'", 'unique': 'True', 'to': u"orm['django_relationship_example.TargetClass']"})
        },
        u'django_relationship_example.targetclass': {
            'Meta': {'object_name': 'TargetClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_relationship_example']