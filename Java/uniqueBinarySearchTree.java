class uniqueBinarySearchTree {
    public int numTrees(int n) {
        int[] G = new int[n + 1];
        for (int i; i <= n; i++) {
            for (int j; j <= i; j++) {
                G[i] += G[j - 1] * G[i - j];
            }
        }
        return G[n];
    }
}
