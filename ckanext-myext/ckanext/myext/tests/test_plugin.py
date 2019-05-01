"""Tests for plugin.py."""
import ckanext.myext.plugin as plugin
from nose.tools import eq_
import ckan.model as model
import ckan.plugins as plugins
import ckan.tests.factories as factories

def mock_session():
  return sessionmaker()

## @TODO I'm not sure how to get a valid session with 
## database engine here
def test_plugin():
    user = factories.Sysadmin()
    model.Session.add(user)
    model.Session.commit()
    context = {
      'user': user,
      'model': model,
      'session': model.Session,
    }
    case_1 = plugin._get_stats(context, 'should_fail')
    case_2 = plugin._get_stats(context, 'user')
    eq_(1,2, 'One equals one')
    eq_(case_1, '----', '"should_fail" is not a valid stat')
    eq_(case_2, 1, '1 dataset should be registered')
