//@(#)UnknownServiceException.java	1.4

package java.net;

import java.io.IOException;

/**
 * Signals that an unknown service exception has occurred.
 */
public class UnknownServiceException extends IOException {

    /**
     * Constructs a new UnknownServiceException with no detail message. 
     * A detail message is a String that gives a specific description
     * of this error. 
     */
    public UnknownServiceException() {
    }

    /**
     * Constructs a new UnknownServiceException with the specified detail message. 
     * A detail message is a String that gives a specific description
     * of this error. 
     * @param msg the detail message
     */
    public UnknownServiceException(String msg) {
	super(msg);
    }
}
