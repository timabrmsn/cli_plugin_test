from distutils.core import setup

setup(
    name="code42cli_users",
    version="0.1",
    packages=["code42cli_users"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_user=code42cli_users.script:get_device_user
    """,
)