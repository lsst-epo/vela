from setuptools import setup

setup(name='astropixie',
      version='0.0.2',
      description='LSST EPO python library.',
      url='https://github.com/lsst-epo/vela',
      author='Christine Banek',
      author_email='cbanek@lsst.org',
      license='MIT',
      packages=['astropixie'],
      include_package_data=True,
      package_data={'astropixie': ['sample_data/*']},
      install_requires=[
        'pytest',
        'numpy',
        'astropy'
      ])
