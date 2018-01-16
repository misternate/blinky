import os


'''
A Link Conditioner wrapper which consumes a profile (Loss, Edge, 3G, etc.)
and invokes the conditioner with the profile.
'''

CONDITIONS = ['100% loss', '3g', 'dsl', 'edge', 'high latency dns', 'very bad network', 'wifi']
OFF_CONDITIONS = ['deactivate', 'disable', 'off', 'kill']

class LinkConditioner():
    def __init__(self, profile):
        self.profile = str.lower(profile)

        if self.profile is not None and self.profile in CONDITIONS or self.profile in OFF_CONDITIONS:
            self.invoke_conditioner()
        else:
            print('Please provide a profile (100% Loss, Edge, 3G, etc.)')

    def invoke_conditioner(self):
        if self.profile in OFF_CONDITIONS:
            self.profile = 'osascript invoke_conditioner.scpt off'
        else:
            self.profile = 'osascript invoke_conditioner.scpt {}'.format(self.profile)
        os.system(self.profile)
        