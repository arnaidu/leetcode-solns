class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0){
            return false;
        }
        else{
            // keep track of open brackets
            char[] open_brackets = new char[s.length()/2 + 1];
            int k = 0;
            int h = 0;
            for (int i = 0; i < s.length(); i++){
                char ch = s.charAt(i);
                if (Character.compare(ch, '(') == 0 || Character.compare(ch, '{') == 0 ||
                    Character.compare(ch, '[') == 0){
                    open_brackets[k] = ch;
                    k++;
                }
                if (Character.compare(ch, ')') == 0 || Character.compare(ch, '}') == 0 ||
                    Character.compare(ch, ']') == 0){
                    if (k == 0 || 
                        Character.compare(open_brackets[k - 1], closedToOpen(ch)) != 0){
                        return false;
                    }
                    else {
                        k--;
                    }
                }
                
            }
            if (k != 0){
                return false;
            }
            return true;
            
        }
        
    }
    public char closedToOpen(char ch){
        if (Character.compare(ch, '}') == 0){
            return '{';
        }
        else if (Character.compare(ch, ']') == 0){
            return '[';
        }
        else{
            return '(';
        }
    }
}
