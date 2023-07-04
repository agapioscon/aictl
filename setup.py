from setuptools import setup, find_packages

setup(
    name='aictl',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'accelerate',
        'controlnet_aux',
        'diffusers',
        'fastapi',
        'mediapipe',
        'opencv-contrib-python',
        'pdf2image',
        'Pillow',
        'pytesseract',
        'torch',
        'torchvision',
        'torchaudio',
        'transformers',
        'uvicorn',
    ],
    extras_require={
        'xformers':  [
            'xformers',
        ],
    },
    entry_points={
        'console_scripts': [
            'aictl = aictl.cli.main:main',
        ],
    },
)