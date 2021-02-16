from distutils.core import setup

setup(
    name="SettingsPlugin",
    version="0.1",
    packages=["c42plug_settings"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_settings=c42plug_settings.script:get_device_settings
    """,
)