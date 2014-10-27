pclm - pseudo clm

This project is a little similar to ccm and jts with a data component.  There are scripts (dockerbuild.sh) scripts to build: pccm, pjts and pdb2 docker images.  There are fig files and data directory in the prodfig/ for example A/B deployment.

When deployed the data directory will need write permissions.

Details:

 - pccm and pjts are a simple python applications.  
 - The pccm application communicates with the pjts via a external url (not a link) notice the JTS environment variable.  This is similar to the way clm is designed.
 - The pdb2 image is a redis database that is used to store a counter.  It allows to demonstration of data migration

See the Dockerfiles and fig files for more information.  It is self documenting.
