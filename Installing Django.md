## Python

We assume you have python 2.7.* already installed. To check if you have python installed, open a terminal window ( on Windows, CMD ) and type the following or copy & paste:

```
python
```

If you see a prompt and some messages like these:

```
Python 2.7.5 (default, Aug 25 2013, 00:04:04)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

Then you have **python** installed. If you do not see anything like the above, then you can go and install **python** from here.
[https://www.python.org/downloads/](https://www.python.org/downloads/)

## Pip

To install pip, download [this file](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) and save to the Desktop.
Next, open your terminal or CMD and cd (change directory) to the desktop.

On Linux, Mac or Ubuntu
```bash
cd /path/to/desktop
```

On Windows
```bash
cd \path\to\Desktop
```

Now run this command.
```bash
python <filename>.py
```

Now you should have pip installed. Restart your terminal or CMD and type.

```bash
pip
```

You should see the documentation that pip come bundled with.

## virtualenv

Virtualenv is not necessary, but it recommended. More information on [http://www.virtualenv.org/en/latest/virtualenv.html](http://www.virtualenv.org/en/latest/virtualenv.html).

To install virtualenv, type the following.

```bash
pip install virtualenv
```

Now you have virtualenv installed.

## Django

To start a Django project, cd into your working directory and type the following:

```bash
virtualenv venv
```

That will create your virtual enviroment.

To activate your virtual enviroment, type the following.

On Linux, Mac, Ubuntu
```bash
source venv/bin/activate
```

On Windows
```bash
venv\Scripts\activate
```

Now you can install Django by typing this:

```bash
pip install django
```

Great now you have Django installed. Enjoy :)
