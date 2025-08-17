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
        'numpy==1.24.4',
        'scikit-learn==1.3.0',
        'scipy==1.10.1',
        'joblib==1.3.2',
        'threadpoolctl==3.2.0',
        'gunicorn==21.2.0',
    ],
    python_requires='>=3.10, <3.11',
)
