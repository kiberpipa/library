from setuptools import setup, find_packages

version = '0.0'

setup(name='liby',
      version=version,
      description="Kiberpipa library.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Kiberpipa',
      author_email='info@kiberpipa.org',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'django-grappelli',
            'django-taggit',
            'django-disqus',
            'south',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
