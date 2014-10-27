#!/bin/bash
( cd db2 ; ./dockerbuild.bash )
( cd ccm ; ./dockerbuild.bash )
( cd jts ; ./dockerbuild.bash )
