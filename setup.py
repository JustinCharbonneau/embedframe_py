from setuptools import setup

setup(name='generate_embedding',
      version='0.1',
      description='Simple library to clean pandas text columns',
      url='https://github.com/justincharbonneau/generate-embedding',
      author='Justin Charbonneau',
      author_email='justin.m.charbonneau@gmail.com',
      license='MIT',
      zip_safe=False,
      install_requires=['pandas'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose']
      )