[source](http://www.windowsecurity.com/uplarticle/14/secure_programming_checklist.txt)

-----BEGIN PGP SIGNED MESSAGE-----

The following is a current check list, in short form, for
quick reference by lab engineers to use in writing secure
Unix code.


This material is excerpted from [or adapted from]
Chapter 23 (page 701) of Practical UNIX and Internet Security by
Simson Garfinkel and Gene Spafford, O'Reilly & Associates,
Sebastopol, CA, 1996, To order, call 1-800-998-9938. You can also
get more information about the book from the WWW URL:

       http://www.ora.com/item/pus2.html

Also, included are inputs from the paper "Enhancing Security of
Unix Systems" by Danny Smith of the Australian Computer
Emergency Response Team. Thanks to both Gene and Danny for
editing this list.


This material is copyright 1996 by O'Reilly & Associates and
by AUSCERT, The University of Queensland, and copies may only
be made provided that:

1) All copies include the copyright notice and full credit information
2) No charge may be made for copies
3) The material is not to be included as part of any other document,
collection or work without express permission of the copyright holders.





        A Lab engineers check list for writing secure Unix code
        -------------------------------------------------------
                                                 Rev.3C 5/23/96


Writing Secure SUID and Network Programs

       The answer is sublime: although the Unix security model is
       basically sound, programmers are careless.  Most security
       flaws in Unix arise from bugs and design errors in programs
       that run as root or with other privileges, or through
       unanticipated interactions of such programs.

      Tips on Avoiding Security-Related Bugs

       When you write a program that will run as superuser or in
       some other critical context, it is important that you try
       to make the program as bug-free as possible.
       Here are some general rules to code by:
       1.  Carefully design the program before you start.
       2.  Check all of your arguments.
       When checking arguments in your program, here are
       specific places to which you should pay attention:
        * Arguments passed to your program on the command line.
        * Arguments that you pass to Unix system functions.
        * Do bounds checking on every variable.
        * Data should be bounded, and verified for syntactic correctness
          integrity, and origin if possible.
        * Arguments you (foolishly) get from the environment
        * Arguments/input you read from a file
        * Typecast variables to what you expect and verify input is
          correct for that type (e.g., passing a large integer to a
          signed int causing it to become negative when you really
          wanted it to be used as positive)

       3.  Don't use routines that fail to check buffer boundaries
           when manipulating strings of arbitrary length.
              AVOID                    USE INSTEAD
               gets                       fgets
               strcpy                     strncpy
               strcat                     strncat
               sprintf                    bcopy
               scanf                      bzero
               sscanf                     memcpy,
                                          memset

           Always do your own variable size calculations correctly.
           i.e., the destination variable must be large enough for
           the stated size being moved.

           NEVER assume that the string is '\0' terminated correctly.
           Bounds check all data manipulation.

           NEVER forget that a string has a '\0' character on the end.
           Therefore, the string "abcde" is *6* bytes long, not 5
           (although strlen says 5)!

       4.  Check all return codes from system calls.  The Unix
           operating system has almost every single system call
           return a return code.

           Do not always assume it will succeed.  Some failures are
           under the control of the user (such as running out of
           process descriptors, file descriptors, free memory, and
           so on).

       5.  Don't have your program depend on Unix environment.
           Some of the things you want to do, therefore, are:
           * If you absolutely must pass information to the program
             in its environment, then have your program test for the
             necessary environment variables and then erase the
             environment completely. Erase what you don't need first,
             get what you want, and kill the remainder.
           * Otherwise, simply wipe the environment clean of all
             but the most essential variables.
           * Make sure that the file descriptors that you expect
             to be open are open and that the file descriptors that
             you expect to be closed are closed. All unnecessary
             file descriptors should be closed before calling  exec().
           * Ensure that your signals are set to a sensible state.
           * Set your umask appropriately.
           * Explicitly chdir to an appropriate directory when the
             program starts.
           * Set whatever limit values are necessary so that your
             program will not leave a core file if it fails.
           * Pass a sensible environment to exec() (not the default
             environment).
       6.  Have internal consistency checking code. For example, use the
           assert macro if programing in C.

       NOTE: that this is not good in production code as it can generate
       a core dump and/or leak potentially sensitive information (such as
       line numbers or assertion expressions).  It is much more designed
       for debug code that can be selectively enabled or disabled.  If
       SIGABRT is not caught, a core dump can be generated.

       The concept of assert macro is good, and the programmer may wish to
       design their own for production purposes that cleans up, reports
       sanitised log information, and exits gracefully.

       7.  Include lots of logging.  Here is specific information
           that you might wish to log:
           * The time that the program was run.
           * The UID and effective UID (also, GID information) of
             the process that ran it.
           * The terminal from which it was run.
           * The process number (PID).
           * Command line arguments.
           * Invalid arguments, or failures in consistency checking.
           * Beware of syslog overflow problems.  Restrict the size
             of the total message that is passed to syslog.
       8.  Make the critical portion of your program as small as
           possible and as simple as possible.
       9.  Read through your code.  Think of how you might attack it
           yourself.  What happens if you provide unexpected output?
           What happens if you are able to delay the program
           arbitrarily between two system calls?
       10. If your program needs to perform some functions as
           superuser, but generally does not require SUID permissions,
           consider putting the SUID part in a different program,
           and constructing a carefully-controlled and monitored
           interface between the two.
       11. If you need SUID or SGID permissions, use them for their
           intended purpose as early in the program as makes sense,
           and then revoke them by returning the effective UID and
           effective GID to those of the process that invoked the
           program.
       12. If you have a program that absolutely must run
           as SUID, try to avoid equipping the program with a
           general-purpose programming interface.
       13. If your program needs special permissions (for example,
           a game program that writes high scores into a particular
           directory), consider having it run SUID to a normal user
           account other than root.
       14. Resist the temptation to make something SUID to root if
           you can accomplish the same goals by making it SGID to a
           new group.
       15. Always use full path names for any argument, for both
           commands and files.
       16. Anything supplied by the user that is then passed on,
           written into a file, or used as a filename should be
           checked for shell meta characters.
           * Don't just check for things like ../ as this can be
             foiled by using tricks such as "."./ if parsed by a shell.
           * Better to check for "valid" characters and discard
             the remainder.
      17. Examine your code and test it carefully for assumptions
           about the operating environments.  For example:
           * If you assume that the program is always run by
             somebody who is not root, what happens if the program
             is run by root?
           * If you assume that it will be run by root, what happens
             if it is not run as root?
           * Many programs designed to be run as daemon or bin can
             cause security programs when run as root.
           * If you assume that it is always run in the /tmp
             directory, what happens if it is run somewhere else?
       18. Make good use of available tools.  If you are using C and
           have an ANSI compiler available, use it, and use prototypes
           for calls.  If you don't have an ANSI C compiler, then
           be sure to use the lint program to check for common mistakes.
       19. Test your program a lot.  If you have a system based on
           SVR4, consider using (at the least) tcov, a statement
           coverage tester.  Consider using commercial products, such
           as CodeCenter and Purify (from personal experience, we
           can tell you that these programs are very useful).  Look
           into GCT, a test tool developed by Brian Marick at the
           University of Illinois.  Remember that it is better to
           find a bug in testing than to let some anonymous system
           cracker find it for you!
       20. Be aware of race conditions.  These can be manifest as a
           deadlock, or as failure of two calls to execute in close
           sequence.
       Deadlock: Remember: more than one copy of your program may be
       running at the same time.  Consider using file locking for any
       files that you modify.  Provide a way to recover the locks in
       the event that the program crashes while a lock is held.  Avoid
       deadlocks and "deadly embraces," which can occur when one
       program attempts to lock file A then file B, while another
       program already holds a lock for file B and then attempts to
       lock file A.

       Sequence: Be aware that your program does not execute atomically.
       That is, the program can be interrupted between any two
       operations and another program run for a while--including
       one that is trying to abuse yours.  Thus, check your code
       carefully for any pair of operations that might fail if
       arbitrary code is executed between them.  The pairs, "stat"...
       "open" and "open"..."chown" are especially notorious.
           * The program environment should *NEVER* be left in a
             vulnerable state even for a single instruction (as above).
       21. Don't have your program dump core.  Instead of dumping
           core, have your program log the appropriate problem and exit.
       22. Avoid shell escapes.
       23. NEVER use system() or popen() calls. execlp and execvp are also
           suspect.
       24. If you are expecting to create a new file with the open
           call, then use the O_EXCL|O_CREAT flags to cause the
           routine to fail if the file exists.  If you expect the
           file to be there, be sure not to include the O_CREAT flag
           so that the routine will fail.
       25. When performing a series of operations on a file, such as
           changing its owner, stating the file, or changing its mode,
           first open the file and then use the fchown(), fstat(),
           or fchmod() system calls.  This will prevent the file from
           being replaced while your program is running (a possible
           race condition).
       26. If you think that a file should be a file, use lstat() to
           make sure that it is not a link.  However, remember that
           what you check may change before you can get around to
           opening it if it is in a public directory (cf#20., above).

        To open a file, which should already exist:

        - lstat() the path, check that lstat succeeded
        - check that it's acceptable (eg, not a symlink)
        - open() (without O_CREAT), check that the open succeeded
        - fstat() the fd returned by open
        - if the lstat and fstat st_ino and st_dev fields match,
          accept.

        To create a new file, which doesn't already exist:

        - lstat() the path, check that you got ENOENT
        - open(...,...|O_CREAT|O_EXCL,...), check that it succeeded

        If you're really paranoid, then:

        - fstat() the fd returned by open
        - lstat() the path again, check that (a) it exists and (b)
          isn't a symlink
        - check that the fstat and the last lstat returned matching
          st_dev and st_ino fields

        NOTE: that the latter depends on the O_CREAT|O_EXCL semantics
        of not following a trailing symlink.






.......................................................................

Item Subject: Sec 2



       27. If you need to create a temporary file, consider using the
           tmpfile() function.  This will create a temporary file,
           open it, delete the file, and return a file handle.
       28. Error recovery. A privileged program can never assume that
           operations will succeed due to its privileged status.
           Recovery should not be attempted unless the recovery is
           guaranteed.
       29. Be aware that /etc/utmp file (which is writeable on some systems)
           can be exploited by careful modification, to write over any
           file on the system, and thus gain privileged access.
           If you must use information from utmp, verify it is correct
           before use.(E.g., if you expect to write to a tty, then the file
           should be something like /dev/ttyxx).
       30. Dynamically linked libraries. It is possible to replace a system
           library with a user created library, if a SUID program calls a
           non-SUID program while still running privileged.
       31. Files that exist outside of the chroot space, that are required by
           the program, must be accessed before the call to chroot().


       Writing SUID/SGID Programs
       1.  "Don't do it.  Most of the time it's not necessary."
       2.  Never write SUID shell scripts.
       3.  If you are using SUID to access a special set of files,
           don't.  Instead, create a special group for your files
           and make the program SGID to THAT GROUP.  If you must use
           SUID, create a special user for the purpose.
       4.  Erase the execution environment, if at all possible, and
           start afresh.  Many security problems have been caused
           because there was a significant difference between the
           environment in which the program was run by an attacker
           and the environment under which the program was developed.
           The entire environment in which the process will be run
           verified and reset by the program. This may involve setting
           known values in environment variables like HOME, PATH, and
           IFS, setting a valid umask value, and initializing all
           variables.
        (Note: if your version of UNIX will allow multiple values in
        the environment with the SAME name, then simply using "getenv"
        and "putenv" for each value is insufficient.  You either need to
        clobber the whole environment and start fresh, or you need to do
        multiple instances of "getenv" to ensure that there are not
        multiple copies of sensitive variables in the environment.)

       5.  Avoid using system() and popen().  If you are using perl,
           try to avoid using pipes. "If you need to spawn extra
           processes, use "fork" with only the execve(2),exec(3) or
           execl(3) calls, and use them with great care. (Avoid the
           execlp(3) and execvp(3) calls.)
       6.  Do not provide shell escapes.  If you must provide them,
           be sure to setgid(getgid()) and setuid(getuid()) before
           executing the user's command. You may need to do a fork
           first if you expect to stay around for additional
           processing.
       7.  In general, use the setuid() and setgid() functions to
           "privilege bracket" your code.  Only turn on the setuid()
           and/or setgid() privilege when it is needed.
       8.  If you must use pipes or subshells, be especially careful
           with the environment variables PATH and IFS.  If at all
           possible, erase these variables and set them to safe values.
           For example:
            putenv ("PATH=/bin:/usr/bin:/usr/ucb");

           NOTE: Ensure that the PATH specification is not
           /bin:/usr/bin:/usr/ucb: (a trailing ":" or empty path name
           such as "::") as this implicitly adds a "." to the PATH.

            putenv ("IFS= \t\r");
           See the Note: under #4
       9.  Use the full path name for all files that you open.  Do not
           make any assumptions about the current directory.  (You
           can enforce this requirement by doing a chdir("/tmp") as
           one of the first steps in your program.)
       10. If you must run as root but only need access to files in a
           specific directory,  You should chdir() to it first, then
           chroot() to that directory. Also, you need to beware in case
           you need other files such as /dev/null, /dev/zero, and
           /dev/log to name a few.
       11. Consider using taintperl for your SUID programs and scripts.
       12. The entire environment in which the process will be run
           should be verified and reset by the program. This may involve
           setting known values in environment variables like HOME,
           PATH, and IFS, setting a valid umask value, and initializing
           all variables.



       PASSWORDS:
       1.  Don't echo the password as the user types it.
       2.  When you store the user's password on the computer, encrypt
           it.  If nothing else, use the crypt(3) library function.
           Use random numbers to choose the password's salt.  When
           the user provides a password, check to see if it is the
           original password by encrypting the provided password with the
           same salt.
       3.  If you need access to crypt(3) from a shell script,
           consider using /usr/lib/makekey, which provides much the
           same functionality.

       Generating Random Numbers:
       A great deal is known about random numbers.  Here are some
        general rules of thumb:
        * If a number is random, then each bit of that number should
          have an equal probability of being a 0 or a 1.
        * If a number is random, then after each 0 in that number
          there should be an equal probability that the following
          bit is a 0 or a 1.  Likewise, after each 1 there should be
          an equal probability that the following bit is a 0 or a 1.
        * If the number has a large number of bits, then there roughly
          half of the number's bits should be 0s, and half of the
          bits should be 1s.
       For security-related purposes, a further requirement for random
       numbers is unpredictably:
        * It should not be possible to predict the output of the
          random number generator given previous outputs or other
          knowledge about the computer generating the random numbers.
        * It should not be possible to determine the internal state
          of the random number generator.
        * It should not be possible to replicate the initial state
          of the random number generator, or to reseed the generator
          with the same initial value.

       Picking a Random Seed
       1.  Seeding a random number generator from a limited space.
       2.  Using a hash value of only the current time as a random seed.
       3.  Divulging the seed value itself.
       4.  Combining some rapidly and constantly changing fields using a
           cryptographically strong hash function.  E.g.;( netstat -a ;
           ps auxww ; vmstat ; who ) | md5

       Some systems may provide a /dev/random device for this purpose.




       So how do you pick a good random number?  Here are some ideas:
        * Use a genuine source of randomness, such as a radioactive
          source, static on the FM dial, thermal noise, or something
          similar.
        * Ask the user to type a set of text, and sample the time
          between keystrokes.
        * Monitor the user.  Each time the user presses the keyboard,
          take the time between the current keypress and the last
          keypress, add it to the current random number seed, and
          hash the result with a cryptographic hash function.  You
          can also use mouse movements to add still more randomness.
        * Avoid relying on the system clock.
        * Don't use Ethernet addresses or hardware serial numbers.
        * Beware of using information such as the time of the
          arrival of network packets.
        * Don't use random selection from a large database.
        * Consider using analog input devices already present on
          your system.


This material is copyright 1996 by O'Reilly & Associates and
by AUSCERT, The University of Queensland, and copies may only
be made provided that:

1) All copies include the copyright notice and full credit information
2) No charge may be made for copies
3) The material is not to be included as part of any other document,
collection or work without express permission of the copyright holders.




-----BEGIN PGP SIGNATURE-----
Version: 2.6.2i
Comment: Finger pgp@ftp.auscert.org.au to retrieve AUSCERT's public key

iQCVAwUBMaWTuSh9+71yA2DNAQFGLgQAkf/J2NbTm+Xyyrbckba4YvMnz2cRHa6a
/br4qrcMnqH5fiBEfhHB4krO3a7kPaUyjO5MrCFdT8gJnU1JZ3coZJHKBqIkF2gv
iQgGemE7p3mIExp1AbOYlrJh08QCCzGCJZKuZ78uMmdtVzjn7pAm0Ma7Rv4l3yXH
NmI55034AvE=
=3rf4
-----END PGP SIGNATURE-----
