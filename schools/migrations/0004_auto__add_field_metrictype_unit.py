# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MetricType.unit'
        db.add_column(u'schools_metrictype', 'unit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MetricType.unit'
        db.delete_column(u'schools_metrictype', 'unit')


    models = {
        u'schools.metric': {
            'Meta': {'object_name': 'Metric'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.MetricType']"}),
            'metric_value': ('django.db.models.fields.TextField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metrics'", 'to': u"orm['schools.School']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Year']"})
        },
        u'schools.metrictype': {
            'Meta': {'object_name': 'MetricType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtype': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'values': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'schools.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['schools']