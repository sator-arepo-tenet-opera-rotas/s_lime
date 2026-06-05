//@(#)DatagramPacket.java	1.7

package java.net;

/**
 * A class that represents a datagram packet containing packet data, packet
 * length, internet addresses and port.
 * @author 	Pavani Diwanji
 */
public final 
class DatagramPacket {
    private byte[] buf;
    private int length;
    private InetAddress address;
    private int port;

    /**
     * This constructor is used to create a DatagramPacket object used 
     * for receiving datagrams.
     * @param ibuf is where packet data is to be received.
     * @param ilength is the number of bytes to be received.
     */
    public DatagramPacket(byte ibuf[], int ilength) {
	if (ilength > ibuf.length) {
	    throw new IllegalArgumentException("illegal length");
	}
	buf = ibuf;
	length = ilength;
	address = null;
	port = -1;
    }
    
    /**
     * This constructor is used construct the DatagramPacket to be sent.
     * @param ibuf contains the packet data.
     * @param ilength contains the packet length
     * @param iaddr and iport contains destination ip addr and port number.
     */
    public DatagramPacket(byte ibuf[], int ilength,
			  InetAddress iaddr, int iport) {
	if (ilength > ibuf.length) {
	    throw new IllegalArgumentException("illegal length");
	}
	buf = ibuf;
	length = ilength;
	address = iaddr;
	port = iport;
    }
    
    public InetAddress getAddress() {
	return address;
    }
    public int getPort() {
	return port;
    }
    public byte[] getData() {
	return buf;
    }
    public int getLength() {
	return length;
    }
}



