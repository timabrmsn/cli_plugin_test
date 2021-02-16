from distutils.core import setup

setup(
    name="SettingsPlugin",
    version="0.1",
    packages=["pkg"],
    install_requires=["code42cli"],
    entry_points="""
        [code42cli.plugins]
        get_device_settings=pkg.script:get_device_settings
    """,
)