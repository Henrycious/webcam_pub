from setuptools import setup

package_name = 'webcam_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='henry gennet',
    maintainer_email='henry.gennet@gmail.com',
    description='Simple Publisher for Microsoft Webcam',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webcam_pub = webcam_pub.publish_cam:main',
            'find_all_cameras = webcam_pub.find_all_cameras:main',
        ],
    },
)
