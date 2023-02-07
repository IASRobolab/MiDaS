from setuptools import setup, find_packages

package_name = 'MiDaS'

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[],
    install_requires=['imutils', 'opencv-python', 'timm', 'einops', 'numpy'],
    zip_safe=True,
    url='https://github.com/IASRobolab/MiDaS',
    maintainer='Federico Rollo',
    maintainer_email='rollo.f96@gmail.com',
    description='Pytorch library of MiDaS for monocular depth estimation',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
)