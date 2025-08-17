from setuptools import setup, find_packages

setup(
    name="cure_cancer_qa",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask==2.3.3',
        'Werkzeug==2.3.7',
        'Jinja2==3.1.2',
        'itsdangerous==2.1.2',
        'click==8.1.7',
        'numpy>=2.3.2',
        'scikit-learn==1.6.1',  # Must match the version used to train the model
        'scipy>=1.16.1',
        'joblib==1.3.2',
        'threadpoolctl==3.2.0',
        'gunicorn',
    ],
    python_requires='>=3.10, <3.11',
)
