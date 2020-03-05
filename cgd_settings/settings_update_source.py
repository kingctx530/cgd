class SettingsUpdateSource:
    def __init__(self):
        self.import_data = [
            'import sys',
        ]

        self.sys_data = [
            'sys.path.insert(0, os.path.join(BASE_DIR, \'apps\'))  # 將未來要使用的套件都導入 apps 裡面',
            'PROJECT_NAME = os.path.basename(os.path.dirname(__file__))',
        ]

        self.asgi_data = [
            'ASGI_APPLICATION = "{}.channels.routing.application".format(PROJECT_NAME)',
        ]

        self.test_apps_data = [
            'TEST_APP = [',
            ']',
        ]

        self.sys_apps_data = [
            'SYS_APP = [',
            '    \'calamus\',   #auto generate app',
            ']',
        ]

        self.install_apps_data = [
            'INSTALLED_APPS = INSTALLED_APPS + SYS_APP + TEST_APP',
        ]

        self.template_data = [
            '        \'DIRS\': [os.path.join(BASE_DIR, \'templates\')],',
        ]

        self.channel_data = ["""
CHANNEL_LAYERS = {
    'default': {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [('192.168.16.123', '6379')],
            "hosts": [('127.0.0.1', '6379')],
        },
        # "ROUTING": "achilles.channel.routing.channel_routing",
    }
}
"""
                             ]

        self.templatetags = """            #for templatetags use        
            'libraries': {
            },
"""

        self.static_data = """
STATIC_ROOT = (
    os.path.join(BASE_DIR, 'staticfiles')
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'public/static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'public/media')
)
"""
