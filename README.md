pclm - pseudo clm

This project is a little similar to ccm and jts with a data component.  There are scripts (dockerbuild.sh) scripts to build: pccm, pjts and pdb2 docker images.  There are fig files and data directory in the prodfig/ for example A/B deployment.

When deployed the data directory will need write permissions.

Step by step
------------

 - git clone thisRepository
 - cd pclm
 - ./dockerbuild.sh
 - docker images

----------
    REPOSITORY           TAG                 IMAGE ID            
    powellquiring/pjts   1.1                 b2daacad9b05
    powellquiring/pccm   1.1                 5fcc27421737
    powellquiring/pjts   1.0                 ce8c527e09c6
    powellquiring/pccm   1.0                 27d23eb4032b
    powellquiring/pdb2   1.0                 988fc7f4264c

 - cd prodfig
 - # if you are running vagrant or boot2docker you will need to do the chmod on the host
 - chmod 777 */*/data
 - cd A
 - fig up
 - # This is your production environment for version 1.0 test it out
 - curl http://localhost:8180

----------
    JTS version 1.1 called 40 times
 - curl http://loclahost:8181

----------
    ccm version 1.1 called 49 times - JTS version 1.1 called 41 times
 -  cd ../B
 - cp ../A/data/* data/*
 - fig up
 - # This is your production environment for the version 1.1 test with copied data
 - curl http://localhost:8280
 - curl http://loclahost:8281

Details
-------

 - pccm and pjts are a simple python applications.  
 - The pccm application communicates with the pjts via a external url (not a link) notice the JTS environment variable.  This is similar to the way clm is designed.
 - The pdb2 image is a redis database that is used to store a counter.  It allows to demonstration of data migration

See the Dockerfiles and fig files for more information.  It is self documenting.
