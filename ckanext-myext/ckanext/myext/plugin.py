import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.model as model
from ckan.common import c

def _get_context():
    return {'model': model,
            'session': model.Session,
            'user': c.user,
            'for_view': True,
            'with_private': False}


def _get_stats(context, arg):
  try:
    action = "{0}_list".format(arg)
    return len(toolkit.get_action(action)(_get_context(), {}))
  except:
    return '----'
  
def get_stats(arg):
  return _get_stats(_get_context(), arg)

class MyextPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'myext')
    
    def get_helpers(self):
      return {
          'myext_get_stats': get_stats
        }
