class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1){
            return strs[0];
        }
        // get current longest prefix as first element
        String longest_prefix = strs[0];
        for (int i = 1; i < strs.length; i++){
            String s = strs[i];
            for (int j = 0; j < longest_prefix.length() && j < s.length(); j++){
                int comp = Character.compare(s.charAt(j), longest_prefix.charAt(j));
                if (comp != 0){
                    if (j == 0){
                        return "";
                    }
                    // longest common prefix is at most this
                    longest_prefix = longest_prefix.substring(0, j);
                    break;
                }
                else{
                    if (j == longest_prefix.length() - 1 || j == s.length() - 1){
                        longest_prefix = longest_prefix.substring(0, j + 1);
                    }
                }
            }
            if (s.length() == 0){
                return "";
            }
        }
        return longest_prefix;
    }
}
