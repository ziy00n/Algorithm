// 백준 2606 바이러스
// DFS

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static int[][] arr;
	static boolean[] visit;
	static int cnt = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st ;
		
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		arr = new int[n+1][n+1];
		visit = new boolean[n+1];
		
		for(int i = 1 ; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
	
			arr[num1][num2] = 1;
			arr[num2][num1] = 1;
		}
	
		System.out.println(dfs(1) - 1);
	}
	
	static int dfs(int num) {
			visit[num] = true;
			cnt++;
			
			for(int i = 1 ; i <= n; i++) {
				if(arr[num][i] == 1 && !visit[i]) {	
					dfs(i);
				}
			}
		return cnt;
	}
}