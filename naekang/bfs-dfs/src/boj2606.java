import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class boj2606 {
    static int n, m;
    static int graph[][];
    static int checked[];

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<Integer>();

        checked[start] = 1;
        q.offer(start);
        int cnt = 0;

        while (!q.isEmpty()) {
            int tmp = q.poll();

            for (int i = 1; i < graph.length; i++) {
                if (graph[tmp][i] == 1 && checked[i] != 1) {
                    q.offer(i);
                    checked[i] = 1;
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        graph = new int[n+1][n+1];
        checked = new int[n+1];

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            graph[x][y] = graph[y][x] = 1;
        }

        bfs(1);
    }
}
