import os


'''
A Link Conditioner wrapper which consumes a profile (Loss, Edge, 3G, etc.)
and invokes the conditioner with the profile.
'''


class LinkConditioner():
    def __init__(self, profile):
        self.profile = profile
        print(profile)
        if self.profile is not None:
            self.invoke_conditioner()
        else:
            print('Please provide a profile (100% Loss, Edge, 3G, etc.)')

    def invoke_conditioner(self):
        if str.lower(self.profile) == 'off':
            self.profile = 'osascript invoke_conditioner.scpt off'
        else:
            self.profile = 'osascript invoke_conditioner.scpt {}'.format(self.profile)
        os.system(self.profile)