# static_html_buildscript
python script to merge static html files for html site builds

buildscript.py works by taking all of the static html files (excluding head.html and foot.html)
and for each one: prepending head.html and foot.html and writing it to the parent directory of the build_files directory.

As an example, the current structure is as follows (when located inside of Project_Directory):

```
Project_Directory
 |-build_files
    |-buildscript.py
    |-example.html
    |-foot.html
    |-head.html
    |-index.html
```

Once buildscript.py runs, it will add the contents of head.html and foot.html to the beginning and end, respectively,
of each file: index.html and example.html and write them to the parent directory (in this case, Project_Directory).
Note that each time buildscript.py runs, it will first remove any existing files in the parent directory that have the same name.
Also note that any references inside of head.html or foot.html to other files currently must use the path relative to the final
file destination, for instance, relative to Project_Directory in the example.

```
Project_Directory
 |-index.html
 |-example.html
 |-build_files
    |-buildscript.py
    |-example.html
    |-foot.html
    |-head.html
    |-index.html
```

In the above example, if example.css and example.js files are located in the following directory structure:

```
Project_Directory
 |-css
 |  |-example.css
 |
 |-js
 |  |-example.js
 |
 |-index.html
 |-example.html
 |-build_files
    |-buildscript.py
    |-example.html
    |-foot.html
    |-head.html
    |-index.html
```

Appropriate filepaths in the html files in build_files would be relative to Project_Directory: css/example.css and js/example.js
instead of ../css/example.css and ../js/example.js

This behavior may be undesired in some text editors that will automatically fill in filepaths.
A future commit *might* include the ability to check and rewrite filepaths as lines are written to the new files.
