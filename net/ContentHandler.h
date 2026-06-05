//@(#)ContentHandler.java	1.4

package java.net;

import java.io.IOException;

/**
 * A class to read data from a URLConnection and construct an
 * Object.  Specific subclasses of ContentHandler handle
 * specific mime types.  It is the responsibility of a ContentHandlerFactory
 * to select an appropriate ContentHandler for the mime-type
 * of the URLConnection.  Applications should never call ContentHandlers
 * directly, rather they should use URL.getContent() or
 * URLConnection.getContent()
 * @author  James Gosling
 */

abstract public class ContentHandler {
    /** 
     * Given an input stream positioned at the beginning of the
     * representation of an object, reads that stream and recreates
     * the object from it. 
     * @exception IOException  An IO error occurred while reading the object.
     */
    abstract public Object getContent(URLConnection urlc) throws IOException;
}

