from setuptools import setup

setup(
	name='branch-and-bound-feature-selection',
	version='0.3',
	description='Implementation of Backward Feature Selection using "Branch and Bound"',
	url='https://github.com/MaximilianIdahl/branch-and-bound-feature-selection',
	author='Maximilian Idahl',
	author_email='max@idahl.de',
	license='MIT',
	packages=['branch_and_bound'],
	install_requires=['numpy>=1.13', 'scikit-learn>=0.19'],
	keywords=['feature selection', 'branch and bound', 'branch', 'bound', 'backward', 'eliminaton']
)
