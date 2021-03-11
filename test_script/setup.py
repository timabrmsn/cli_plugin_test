from distutils.core import setup

setup(
    name="script",
    version="0.2",
    py_modules=["script"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        my_command=script:my_command
    """,
)