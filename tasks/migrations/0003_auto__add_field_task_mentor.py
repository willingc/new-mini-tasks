# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.mentor'
        db.add_column(u'tasks_task', 'mentor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.mentor'
        db.delete_column(u'tasks_task', 'mentor')


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
            'env_difficulty': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mentor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
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