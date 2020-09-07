class trappingRainWater {
    public int trap(int[] height) {
        int maxR = Integer.MAX_VALUE * -1;
        int maxL = Integer.MAX_VALUE * -1;
        int[] rightMaxArr = new int[height.length];
        int[] leftMaxArr = new int[height.length];
        int ans = 0;
        for(int i=0; i<height.length; i++) {
            if(height[i]>maxL) {
                maxL = height[i];
                leftMaxArr[i] = height[i];
            } else {
                leftMaxArr[i] = maxL;
            }
        }
        for(int i=height.length-1; i>=0; i--) {
            if(height[i]>maxR) {
                maxR = height[i];
                rightMaxArr[i] = height[i];
            } else {
                rightMaxArr[i] = maxR;
            }
        }
        for(int i=0; i<height.length; i++){
            ans += Math.min(leftMaxArr[i], rightMaxArr[i]) - height[i];
        }
        return ans;
    }
}
