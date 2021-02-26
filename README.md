# WaterReminder

----
A program written in both Java and Python to remind yourself to drink
water while you are on your computer throughout the day.

This program runs in the background and periodically will 
play a sound clip that reminds you to drink some water. 
Both the periodic interval and sound clips are editable 
for the user.
----

##Configuration File

----
The configuration file for this project is as follows:
```yaml
###############################
# WaterReminder Configuration #
###############################
# Learn the YAML format at https://www.yaml.org/ before editing this file.

# The path to the directory that with the audio files for reminding yourself
# to drink water (string).
#
# NOTE: That the source directory is the directory where you run the program
#       and is the default starting place of a Path.
#       Use '../' to go up a directory.
audio-path: 'reminder-audio/'

# The interval between each reminder of drinking water in minutes.
#
# The actual interval between each reminder is a random number between the
# maximum and minimum number of minutes.
#
# @minimum-interval: The minimum amount of minutes before a reminder (integer).
# @maximum-interval: The maximum amount of minutes before a reminder (integer).
minimum-interval: 60
maximum-interval: 90
```
----

##Future Plans

----
- Create the Java version of the program.
- Convert the Python program to an executable file.
- Have command processing during the program.
  - **/reload** command to reload the configuration values.
  - **/pause** to pause the program.
  - **/interval** to view the interval and time left until next reminder.
  - **/stats** general statistics command.
  - **/quit** quits the program.
- Add a custom interface for the program with buttons to make it easier to
operate.
- Have the reminder optionally give you a system notification too.
----

##Open Source Project

----
This project operates under the MIT License and is completely open source. 
Feel free to submit any pull requests or issues as you please.
----