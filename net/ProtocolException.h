//@(#)ProtocolException.java	1.6

package java.net;

import java.io.IOException;

/**
 * Signals when connect gets an EPROTO.  This exception is specifically
 * caught in class Socket.
 * @version 1.6, 08/16/95
 * @author Chris Warth
 */
public 
class ProtocolException extends IOException { 

    /**
     * Constructs a new ProtocolException with the specified detail 
     * message.
     * A detail message is a String that gives a specific description
     * of this error. 
     * @param host the detail message
     */
    public ProtocolException(String host) {
	super(host);
    }
    
    /**
     * Constructs a new ProtocolException with no detail message.
     * A detail message is a String that gives a specific description
     * of this error.  
     */
    public ProtocolException() {
    }
}
