class Solution {
    public int reverse(int x) {
        // Integer.MAX_VALUE = 2147483647
        // Integer.MIN_VALUE = -2147483648
        int result = 0;

        while (x != 0) {
            int digit = x % 10; // Grabs the left most value
            x /= 10; // Cut off the leftmost digit

            // Check for overflow
            if (result > Integer.MAX_VALUE / 10
                || (result == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }

            if (result < Integer.MIN_VALUE / 10
                || (result == Integer.MIN_VALUE / 10 && digit < -8)) {
                return 0;
            }

            result = result * 10 + digit;
        }
        return result;
    }
}
