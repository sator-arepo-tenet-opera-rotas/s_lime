//@(#)MalformedURLException.java	1.6

package java.net;

import java.io.IOException;

/**
 * Signals that a malformed URL has occurred.
 * @version 1.6, 09/08/95
 * @author 	Arthur van Hoff
 */
public class MalformedURLException extends IOException {

    /**
     * Constructs a MalformedURLException with no detail message.  A
     * detail message is a String that describes this particular 
     * exception.
     */
    public MalformedURLException() {
    }

    /**
     * Constructs a MalformedURLException with the specified detail 
     * message.  A detail message is a String that describes this 
     * particular exception.
     * @param msg the detail message
     */
    public MalformedURLException(String msg) {
	super(msg);
    }
}
