md5-collision-finder
====================

A Python code that find collisions in MD5 hashes. It can be fully customized to test not only MD5. You can also change the hash length to reduce time. The strings used to generate the hashes are random. In practitcal, it seems more faster.

Juste run the command:

python MD5Collisions.py

As explained in the code, it will prompt a message every 100000 tests so don't panic.

- In the end, it will prompt the list of string which generate similar hashes. Keep in mind that they are only similar for a portion of the hash (except if you have generate a full length hash)

- It also have a cool feature to limit the use of RAM. You can't set a limit to not destroy your system and be able to leave your computer during processing.

- Only tested on Linux Ubuntu 11.04

Licence GPL GNU
