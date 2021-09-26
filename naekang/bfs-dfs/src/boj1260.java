import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class boj1260 {

    static int N, M, V;
    static int[][] graph = new int[1001][10001];
    static boolean[] checked = new boolean[1001];

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();

        for (int i = 0; i < M; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            graph[x][y] = graph[y][x] = 1;
        }

        dfs(V);

        checked = new boolean[10001];
        System.out.println();
        bfs();
    }

    public static void bfs() {
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(V);
        checked[V] = true;
        System.out.print(V + " ");

        while (!q.isEmpty()) {
            int tmp = q.poll();

            for (int j = 1; j <= N; j++) {
                if (graph[tmp][j] == 1 && checked[j] == false) {
                    q.offer(j);
                    checked[j] = true;
                    System.out.print(j + " ");
                }
            }
        }
    }

    public static void dfs(int x) {
        checked[x] = true;
        System.out.print(x + " ");

        for (int i = 1; i <= N; i++) {
            if (graph[x][i] == 1 && checked[i] == false) {
                dfs(i);
            }
        }
    }
}
