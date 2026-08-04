//@(#)UnknownHostException.java	1.5

package java.net;

import java.io.IOException;

/**
 * Signals that the address of the server specified by a network client could not
 * be resolved.
 * 
 * @version     1.5,08/16/95
 * @author      Jonathan Payne 
 */
public 
class UnknownHostException extends IOException {
    
    /**
     * Constructs a new UnknownHostException with the specified detail message.
     * A detail message is a String that gives a specific description
     * of this error. 
     * @param host the detail message
     */
    public UnknownHostException(String host) {
	super(host);
    }

    /**
     * Constructs a new UnknownHostException with no detail message. 
     * A detail message is a String that gives a specific description
     * of this error.  
     */
    public UnknownHostException() {
    }
}

