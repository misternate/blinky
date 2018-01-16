# Link Conditioner Wrapper
This is a small utility that makes it easy to invoke Apple's Link Conditioner, to throttle your connection, from within your Python script. The utility supports setting a network profile and setting a time duration. This utility can be useful if you want to throw a few network conditions in to your end-to-end tests. 

To get started:
1. Clone the repository.
2. Allow your environment (terminal, VS Code, PyCharm, etc.) to control your computer. This is required to access Prefs from within your script. _System Preferences > Security & Privacy > Privacy > + in Add the apps below to control your computer_.
3. `import link_conditioner`; pass a pre-defined or custom network profile; and set a duration (optional).  