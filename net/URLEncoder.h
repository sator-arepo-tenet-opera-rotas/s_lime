//@(#)URLEncoder.java	1.4 95/12/18 

package java.net;

import java.io.ByteArrayOutputStream;
import java.util.BitSet;


/**
 * Turns Strings of text into x-www-form-urlencoded format.
 *
 * @version 1.4, 12/18/95
 * @author Herb Jellinek
 */

public class URLEncoder {

    static BitSet dontNeedEncoding;

    static {
	dontNeedEncoding = new BitSet(256);
	int i;
	for (i = 'a'; i <= 'z'; i++) {
	    dontNeedEncoding.set(i);
	}
	for (i = 'A'; i <= 'Z'; i++) {
	    dontNeedEncoding.set(i);
	}
	for (i = '0'; i <= '9'; i++) {
	    dontNeedEncoding.set(i);
	}
	dontNeedEncoding.set('_');
	dontNeedEncoding.set(' ');
    }

    /**
     * You can't call the constructor.
     */
    private URLEncoder() { }

    /**
     * Translates String into x-www-form-urlencoded format.
     * @param s String to be translated
     * @return the translated String.
     */
    public static String encode(String s) {
	ByteArrayOutputStream out = new ByteArrayOutputStream(s.length());
	
	for (int i = 0; i < s.length(); i++) {
	    int c = (int)s.charAt(i);
	    if (dontNeedEncoding.get(c)) {
		if (c == ' ') {
		    c = '+';
		}
		out.write(c);
	    } else {
		out.write('%');
		out.write(Character.forDigit(c >> 4, 16));
		out.write(Character.forDigit(c & 0xF, 16));
	    }
	}

	return out.toString();
    }
}
