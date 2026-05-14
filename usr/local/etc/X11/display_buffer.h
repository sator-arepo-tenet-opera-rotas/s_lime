GsDefDispBuff(0, 0, 0, 240); /* Initializes the double buffers */ 
/* in memory and specifies clipping */ 
/* parameters. */ 

/* For (0,0)-(320,240), display (0,240)- (320,480) (db[0]) */ 

/* For (0,240)-(320,480), display (0,0)- (320,240) (db[0]) */ 


/* Ordering table information setting */ 
for (i = 0; і < 2; і++) 
{ 


31 


32 


WorldOT[i].length = OT LENGTH; 
WorldOT[i].org = OTTags[i]; 
} 
