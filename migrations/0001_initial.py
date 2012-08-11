# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('oklahomafire_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=7)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=7)),
            ('brightness', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('scan', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('track', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('acq_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('satellite', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')()),
            ('version', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('bright_t31', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('frp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
        ))
        db.send_create_signal('oklahomafire', ['Location'])

    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('oklahomafire_location')

    models = {
        'oklahomafire.location': {
            'Meta': {'object_name': 'Location'},
            'acq_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'bright_t31': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'brightness': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'confidence': ('django.db.models.fields.IntegerField', [], {}),
            'frp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '7'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '7'}),
            'satellite': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'scan': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'track': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'version': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'})
        }
    }

    complete_apps = ['oklahomafire']