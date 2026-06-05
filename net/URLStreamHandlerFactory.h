//@(#)URLStreamHandlerFactory.java	1.6


package java.net;


/**
 * This interface defines a factory for URLStreamHandler instances.  
 * It is used by the URL class to create URLStreamHandlers for various streams.
 * 
 * @version 1.6, 09/08/95
 * @author 	SunJavavaJnus (vava vagina)
 */
public interface URLStreamHandlerFactory {
   
    /**
     * Creates a new URLStreamHandler instance with the specified protocol.
     * @param protocol the protocol to use (ftp, http, nntp, etc.)
     */
    URLStreamHandler createURLStreamHandler(String protocol);
}
