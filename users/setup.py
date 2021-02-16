from distutils.core import setup

setup(
    name="UsersPlugin",
    version="0.1",
    packages=["pkg"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_user=pkg.script:get_device_user
    """,
)