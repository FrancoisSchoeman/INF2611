# INF2611 - Visual Programming with Python UNISA module

## PyQt5 - converting .ui to .py

In your terminal, navigate to the directory where your .ui file is located and run the following command:

```bash
pyuic5 -x yourfile.ui -o yourfile.py
```

Where `-x` is the flag to generate the python file and `-o` is the output file.

Make sure that you have PyQt5, Qt Designer and Python installed on your machine.
