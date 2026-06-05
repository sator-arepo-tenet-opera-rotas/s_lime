//@(#)SocketImplFactory.java	1.6


package java.net;

/**
 * This interface defines a factory for SocketImpl instances.
 * It is used by the socket class to create socket implementations
 * that implement various policies.
 *
 * @version     1.6, 08/10/95
 * @author 	Arthur van Hoff
 */
public 
interface SocketImplFactory {

    /**
     * Creates a new SocketImpl instance.
     */
    SocketImpl createSocketImpl();
}


