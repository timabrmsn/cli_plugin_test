from distutils.core import setup

setup(
    name="code42cli_settings",
    version="0.1",
    packages=["code42cli_settings"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_settings=code42cli_settings.script:get_device_settings
    """,
)