public class HebbianLearning {
 public static void main(String[] args) {
 int[][] X = {
 {1, 1},
 {1, -1},
 {-1, 1},
 {-1, -1}
 };
 int[] T = {1, -1, -1, -1};
 int[] w = {0, 0};
 double b = 0.0;
 for (int i = 0; i < X.length; i++) {
 w[0] = w[0] + X[i][0] * T[i];
 w[1] = w[1] + X[i][1] * T[i];
 b = b + T[i];
 }
 for (int i = 0; i < X.length; i++) {
 int net = X[i][0] * w[0] + X[i][1] * w[1];
 net = net + (int)b;
 int output = (net >= 0) ? 1 : -1;
 System.out.println("Input: " + X[i][0] + ", " + X[i][1]);
 System.out.println("Net Input: " + net);
 System.out.println("Output: " + output);
 System.out.println("Target: " + T[i]);
 System.out.println();
 }
 }
}