//@(#)ContentHandlerFactory.java	1.1

package java.net;


/**
 * This interface defines a factory for ContentHandler instances.  It is used by the
 * URLStreamHandler class to create ContentHandlers for various streams.
 * 
 * @version 1.1, 08/20/95
 * @author James Gosling
 */
public interface ContentHandlerFactory {
   
    /**
     * Creates a new ContentHandler to read an object from a URLStreamHandler.
     * @param mimetype	The mime type for which a content handler is desired.
     */
    ContentHandler createContentHandler(String mimetype);
}
