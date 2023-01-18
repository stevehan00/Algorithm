class Solution {
    public int numIslands(char[][] grid) {
		Queue<Dot> qu = new LinkedList<>();
		
		int cnt = 0;
		
		for(int i = 0; i < grid.length; i++) {
			for(int j = 0; j < grid[i].length; j++) {
				if(grid[i][j] == '1') {
					cnt++;
					grid[i][j] = 0;
					qu.offer(new Dot(i, j));
					while(!qu.isEmpty()) {
						Dot temp = qu.poll();
                
						if(temp.x+1 < grid.length && grid[temp.x+1][temp.y] == '1') {
							grid[temp.x+1][temp.y] = 0;
							qu.offer(new Dot(temp.x+1, temp.y));
						}
						
						if(temp.x-1 >= 0 && grid[temp.x-1][temp.y] == '1') {
							grid[temp.x-1][temp.y] = 0;
							qu.offer(new Dot(temp.x-1, temp.y));
						}
						
						if(temp.y+1 < grid[i].length && grid[temp.x][temp.y+1] == '1') {
							grid[temp.x][temp.y+1] = 0;
							qu.offer(new Dot(temp.x, temp.y+1));
						}
						
						if(temp.y-1 >= 0 && grid[temp.x][temp.y-1] == '1') {
							grid[temp.x][temp.y-1] = 0;
							qu.offer(new Dot(temp.x, temp.y-1));
						}
					}
				}
			}
		}
		
		return cnt;
    }

}

class Dot{
	int x;
	int y;
	
	public Dot(int x, int y){
		this.x = x;
		this.y = y;
	}
}