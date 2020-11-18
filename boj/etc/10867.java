import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Vector vc = new Vector();
		
		int amt = sc.nextInt();
		
		for(int i = 0; i<amt; i++) {
			int a = sc.nextInt();
			vc.add(a);
		}
		
		Object[] objs = vc.toArray();
		Arrays.sort(objs);
		
		ArrayList<Integer> arr = new ArrayList<>();
		
		for(int i = 0; i<vc.size(); i++) {
			if(!arr.contains(objs[i]))
				arr.add((int)objs[i]);
		}
		
		
		for (int i=0; i < arr.size(); i++){

		       System.out.print(arr.get(i) + " ");

		}



	}
}
