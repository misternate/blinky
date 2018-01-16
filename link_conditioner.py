import os
import time


'''
This Link Conditioner wrapper takes a network profile (Loss, Edge, 3G, etc.)
and duration. If a duration is passed, the Conditioner will stay ON for
the set time. Otherwise, the Conditioner will remain ON indefinitely.
'''

CONDITIONS = ['100% loss', '3g', 'dsl', 'edge', 'high latency dns', 'very bad network', 'wifi']
OFF_CONDITIONS = ['deactivate', 'disable', 'off', 'kill']


class LinkConditioner():
    def __init__(self, profile, duration=None):
        self.profile = str.lower(profile)
        self.duration = duration

        if self.profile is not None and self.profile in CONDITIONS or self.profile in OFF_CONDITIONS:
            self.invoke_conditioner()
        else:
            print('Please provide a profile (100% Loss, Edge, 3G, etc.)')

    def invoke_conditioner(self):
        if self.profile in OFF_CONDITIONS:
            self.deactivate_conditioner()
        else:
            if self.duration is None:
                self.activate_conditioner()
            else:
                self.activate_conditioner()
                self.timer()

    def deactivate_conditioner(self):
        profile = 'osascript invoke_conditioner.scpt off'
        os.system(profile)

    def activate_conditioner(self):
        profile = 'osascript invoke_conditioner.scpt {}'.format(self.profile)
        os.system(profile) 

    def timer(self):
        seconds = int(self.duration)
        start = time.time()
        time.clock()
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start + 1
            time.sleep(1)
        self.deactivate_conditioner()
