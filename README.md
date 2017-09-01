# Simple Python Key Logger
NSK is a simple and easy to use key logger written in python. NSK is available to use under MIT License.

# Dependencies
NSK (Simple python key logger) uses the following python libraries / pip packages.

  - [PyObjC](https://en.wikipedia.org/wiki/PyObjC)

# How to use

**1: clone the repository first.**
```
git clone https://github.com/amyth/nsk
cd nsk
```

**2: create a virtual environment**

Make sure you have [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) installed. Then create a new virtual environment and install the dependencies.

```
mkvirtualenv nsk
pip install -r requirements/pip.txt
```

**3: start the key logger**
Once you have all the dependencies installed, you can simply start the key logger using the following command.

```
python nskl.py
```

If you'd like to hide the output on the terminal, you can use [Screen](https://help.ubuntu.com/community/Screen) (terminal multiplexer) and run the keylogger on a screen and detach from the screen. The key logger will still print all system wide input.

**4: The Logs**
In addition to the terminal output `nsk` also saves the copy to the logs that can be found at the following location:

```
/var/log/nskl/
```
# Sample Output

Following is the sample output produced by the keylogger

```
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4208.2 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="h" unmodchars="h" repeat=0 keyCode=4>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4208.3 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="e" unmodchars="e" repeat=0 keyCode=14>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4208.4 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="l" unmodchars="l" repeat=0 keyCode=37>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4208.6 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="l" unmodchars="l" repeat=0 keyCode=37>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4208.7 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="o" unmodchars="o" repeat=0 keyCode=31>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4209.2 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars=" " unmodchars=" " repeat=0 keyCode=49>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4209.3 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="w" unmodchars="w" repeat=0 keyCode=13>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4209.4 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="o" unmodchars="o" repeat=0 keyCode=31>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4209.7 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="r" unmodchars="r" repeat=0 keyCode=15>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4209.9 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="l" unmodchars="l" repeat=0 keyCode=37>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4210.1 flags=0x100 win=0x0 winNum=0 ctxt=0x0 chars="d" unmodchars="d" repeat=0 keyCode=2>
<native-selector keyCode of NSEvent: type=KeyDown loc=(282.23,181.375) time=4210.6 flags=0x20104 win=0x0 winNum=0 ctxt=0x0 chars="!" unmodchars="!" repeat=0 keyCode=18>
```

# Author(s)
 - Amyth [twitter/@mytharora](https://twitter.com/mytharora)
