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



main () 
{ 
int nobj = 1; /* Number of sprites displayed (froml)*/ 
GsOT *ot; /* Pointer to drawing OT */ 


/* 


TAG! Gy Ent Xy y; /* Working variables*/ 
int  activeBuff; 

GsSPRITE  *sp; 

POS pos[MAXOBJ]; 

POS *pp; 


SetVideoMode( MODE NTSC ); /* NTSC Mode */ 
SetVideoMode( MODE PAL ); /* PAL Mode (for European televisions*/ 


GetPadBuf (£bb0, &bbl); /* Get controller reception buffer */ 
datafile search(); /* Data file retrieval  */ 
datafile read(); /* Data file reading */ 


GsInitGraph (320,240,4,0,0); /* Initializes the graphics system  */ 
/* Turn on the GPU, Set background color to black */ 
/* and initializes screen coordinates. */ 



