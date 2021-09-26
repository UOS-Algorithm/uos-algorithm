import java.util.Arrays;
import java.util.Scanner;

public class boj2667 {

    public static int n;
    public static int apartNum = 0;
    public static int dx[] = {0, 0, 1, -1};
    public static int dy[] = {1, -1, 0, 0};
    public static int[] apart = new int[25 * 25];
    public static int[][] map = new int[25][25];
    public static boolean[][] visited = new boolean[25][25];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        map = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String input = sc.next();
            for (int j = 0; j < n; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1 && visited[i][j] == false) {
                    apartNum++;
                    dfs(i, j);
                }
            }
        }

        Arrays.sort(apart);
        System.out.println(apartNum);

        for (int i = 0; i < apart.length; i++) {
            if (apart[i] != 0) {
                System.out.println(apart[i]);
            }
        }

    }

    public static void dfs(int x, int y) {
        visited[x][y] = true;
        apart[apartNum]++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                if (map[nx][ny] == 1 && visited[nx][ny] == false) {
                    dfs(nx, ny);
                }
            }
        }
    }
}
