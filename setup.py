import os
import sys
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))

base_config = {'name': 'model_ninja',
               'version': '0.0.1',
               'description': 'Django libraries to facilitate hiding models instead of deleting them.',
               'long_description': open(os.path.join(ROOT, 'README.md')).read(),
               'author': 'J Leadbetter',
               'author_email': 'codemonkey@jleadbetter.com',
               'url': 'http://bitbucket.org/kamni/django-model-ninja',
               'license': 'Affero GPL v3',
               'include_package_data': True,
               'zip_safe': False,
               'install_requires': ['Django>=1.5'],
               'classifiers': ['Development Status :: 2 - Pre-Alpha',
                               'Environment :: Web Environment',
                               'Framework :: Django',
                               'Intended Audience :: Developers',
                               'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                               'Programming Language :: Python :: 2 :: Only']
              }
                        
if 'develop' in sys.argv:
    base_config.update({'packages': find_packages(),
                        'tests_require': ['django-nose>=1.2']})
else:
    base_config['packages'] = find_packages(exclude=['model_ninja.tests'])

setup(**base_config)
