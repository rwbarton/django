from django.core.management.base import AppCommand


class Command(AppCommand):
    help = 'Test Application-based commands'
    requires_model_validation = False
    args = '[app_label ...]'

    def handle_app_config(self, app_config, **options):
        print('EXECUTE:AppCommand name=%s, options=%s' % (app_config.name, sorted(options.items())))
