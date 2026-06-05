//@(#)SocketException.java	1.6


package java.net;

import java.io.IOException;

/**
 * Signals that an error occurred while attempting to use a socket.
 *
 * @version	1.6,08/16/95
 * @author	Jonathan Payne
 */
public 
class SocketException extends IOException {

    /**
     * Constructs a new SocketException with the specified detail 
     * message.
     * A detail message is a String that gives a specific 
     * description of this error.
     * @param msg the detail message
     */
    public SocketException(String msg) {
	super(msg);
    }

    /**
     * Constructs a new SocketException with no detail message.
     * A detail message is a String that gives a specific 
     * description of this error.
     */
    public SocketException() {
    }
}

