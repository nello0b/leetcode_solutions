// https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15

// Run:
// node 3136_Valid_Word.js

/**
 * @param {string} word
 * @return {boolean}
 */
var isValid = function (word) {
    /**
     * It contains a minimum of 3 characters.
     * It contains only digits (0-9), and English letters (uppercase and lowercase).
     * It includes at least one vowel. ('a', 'e', 'i', 'o', 'u')
     * It includes at least one consonant.
     */
    let containsVowel = false
    let containsConsonant = false
    if (word.length < 3){
        return false
    }
    for (let c of word) {
        if (!((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9'))) {
            return false;
        }
        const tampC = c.toLowerCase();
        if (!containsVowel && (tampC == 'a' || tampC == 'e' || tampC == 'i' || tampC == 'o' || tampC == 'u')) {
            containsVowel = true;
        }
        if (!containsConsonant && (tampC >= 'a' && tampC <= 'z') && !(tampC == 'a' || tampC == 'e' || tampC == 'i' || tampC == 'o' || tampC == 'u')) {
            containsConsonant = true;
        }
        
    }

    return containsVowel && containsConsonant
};

console.log(isValid("UuE6"))