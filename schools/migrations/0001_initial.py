# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Year'
        db.create_table(u'schools_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'schools', ['Year'])

        # Adding model 'School'
        db.create_table(u'schools_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'schools', ['School'])

        # Adding model 'MetricType'
        db.create_table(u'schools_metrictype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('mtype', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'schools', ['MetricType'])

        # Adding model 'Metric'
        db.create_table(u'schools_metric', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.Year'])),
            ('metric_value', self.gf('django.db.models.fields.TextField')()),
            ('metric_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.MetricType'])),
        ))
        db.send_create_signal(u'schools', ['Metric'])


    def backwards(self, orm):
        # Deleting model 'Year'
        db.delete_table(u'schools_year')

        # Deleting model 'School'
        db.delete_table(u'schools_school')

        # Deleting model 'MetricType'
        db.delete_table(u'schools_metrictype')

        # Deleting model 'Metric'
        db.delete_table(u'schools_metric')


    models = {
        u'schools.metric': {
            'Meta': {'object_name': 'Metric'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.MetricType']"}),
            'metric_value': ('django.db.models.fields.TextField', [], {}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.School']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schools.Year']"})
        },
        u'schools.metrictype': {
            'Meta': {'object_name': 'MetricType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mtype': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
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