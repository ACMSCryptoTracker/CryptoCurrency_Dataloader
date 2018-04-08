from celery.schedules import crontab


CELERY_IMPORTS = ('app.tasks.test','app.tasks.graphGeneration')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'app.tasks.test.insertIntoDatabase',
        # Every minute
        'schedule': crontab(minute="*/5")
    },
    'test-graph_day' : {
	'task':'app.tasks.graphGeneration.GraphCreationDay',
        'schedule': crontab(minute="*/5")
	},
    'test_graph_month' : {
	 'task':'app.tasks.graphGeneration.GraphCreationMonth',
	  'schedule':crontab(minute="*/5 ")
     },
     'compare_graph_day' : {
	  'task':'app.tasks.graphGeneration.ComparisonGraphDay',
	   'schedule':crontab(minute="*/5")
     },
     'compare_graph_month' : {
	   'task':'app.tasks.graphGeneration.ComparisonGraphMonth',
	   'schedule' : crontab(minute="*/5")
	}
}
