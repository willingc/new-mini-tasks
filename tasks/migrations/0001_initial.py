# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('item_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('skills', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('community_tools', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('suggested_for', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('suggested_mode', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('recently_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tasks', ['Task'])

        # Adding model 'Student'
        db.create_table(u'tasks_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
        ))
        db.send_create_signal(u'tasks', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'tasks_task')

        # Deleting model 'Student'
        db.delete_table(u'tasks_student')


    models = {
        u'tasks.student': {
            'Meta': {'object_name': 'Student'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Task']"})
        },
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'community_tools': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recently_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skills': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suggested_for': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suggested_mode': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tasks']