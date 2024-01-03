
0. Readme
mandatory

Write a script that reads and prints the content of a file.

    The first argument is the file path
    The content of the file must be read in utf-8
    If an error occurred during the reading, print the error object

guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 


1. Write me
mandatory

Write a script that writes a string to a file.

    The first argument is the file path
    The second argument is the string to write
    The content of the file must be written in utf-8
    If an error occurred during while writing, print the error object

guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 


2. Status code
mandatory

Write a script that display the status code of a GET request.

    The first argument is the URL to request (GET)
    The status code must be printed like this: code: <status code>
    You must use the module request

guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 


