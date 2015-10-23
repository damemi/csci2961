import java.*;


public class BinarySearchTest {
    public static void main(String args[]) {
	int[] a = new int[10];
	for(int i=0; i<10; i++) {
	    a[i] = i;
	}
	System.out.println(binarySearch(a, Integer.parseInt(args[0])));
    }

    static int binarySearch(int[] a, int x) {
	int el = a.length / 2;
	if(el <= 1) {
	    if(a[el] == x) return 1;
	    else return 0;
	}
	int[] b;
	if(a.length%2 == 1)
	    b = new int[el+1];
	else
	    b = new int[el];
	if(a[el] < x) {
	    for (int i=el; i<a.length; i++) {
		b[i-el] = a[i];
	    }
	    binarySearch(b,x);
	} else if(a[el] > x) {
	    for(int i=0; i<el; i++) {
		b[i] = a[i];
	    }
	    binarySearch(b,x);
	} else {
	    return 1;
	} 
	return 0;
    }
}