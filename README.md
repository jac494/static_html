# Static HTML Build Script

### Description
Create a  static HTML design template to outline a project by merging all files with \
a `.html` extension  with a preconfigured header and footer to allow you to focus on \
 a modular build of static templates for outlining projects.

### Installation (install.py)
* Download the tar.gz file and run `install.py`.
* This creates the File System Structure(defined below) and an alias named `merge`.
* The merge alias allows for `merge.py` to run on your project dir.

##### File system structure
```
* ~/.buidconfig
    *  /config
        *  header.html
        *  footer.html
```
### Build a project (buildscript.py)
Alias: `build-project  {/path/and/projectname}`\
This will create a directory with the 'Project name' and add two files. 
* header.html
* footer.html

##### Project file structure

```
* /path/to/projectName
    *  header.html
    *  footer.html
```

### How To Run
`user@domain$  merge `\
This will take all the files ending with `.html` and prepend `header.html` and append  `footer.html`.

### Open Source License
MIT License

Copyright (c) 2017 Gerald Wells

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
