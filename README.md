# Link Conditioner Wrapper
This is a small utility that makes it easy to invoke Apple's Link Conditioner from within your Python script. The utility supports setting a profile and turning the service on or off.

To get started:
1. Clone the repository.
2. Allow your environment (terminal, VS Code, PyCharm, etc.) to control your computer. This is required to access Prefs from within your script. _System Preferences > Security & Privacy > Privacy > + in Add the apps below to control your computer_.
3. `import link_conditioner` and call with a pre-defined or custom profile.  