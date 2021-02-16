from distutils.core import setup

setup(
    name="UsersPlugin",
    version="0.1",
    packages=["c42plug_users"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_user=c42plug_users.script:get_device_user
    """,
)