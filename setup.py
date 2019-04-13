from setuptools import setup


setup_args = {
    'name':         'testing_demo',
    'author':       'Adrian Liu',
    'url':          'https://github.com/acliu/testing_demo',
    'description':  'Testing demonstration',
    'packages':     ['testing_demo'],
    'package_dir':  {'testing_demo': 'code'},
    'install_requires': ['numpy>=1.15'],
    'zip_safe':     False,
}

if __name__ == '__main__':
    setup(**setup_args)