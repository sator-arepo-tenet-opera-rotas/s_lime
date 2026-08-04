#!/bin/csh -f

cd /opt/carsi/spool
foreach i (*)
        echo '^[%-12345X@PJL RDYMSG DISPLAY="INSERT 5 CENTS"' | netto $i 9100
end
