import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class boj7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        HashMap<String, String> map = new HashMap<>();
        ArrayList<String> arr = new ArrayList<>();

        while (N-- > 0) {
            String[] member = br.readLine().split(" ");
            map.put(member[0], member[1]);
        }

        for (String key : map.keySet()) {
            if (map.get(key).equals("enter")) {
                arr.add(key);
            }
        }

        Collections.sort(arr);

        for (int i = arr.size()-1; i > -1; i--) {
            System.out.println(arr.get(i));
        }
    }
}
