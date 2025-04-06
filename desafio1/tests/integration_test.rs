use desafio1::reverse_string;

#[test]
fn test_reverse_string() {
    let input = "abc";
    let expected = "cba";
    assert_eq!(reverse_string(input), expected);
}

#[test]
fn test_empty_string() {
    let input = "";
    let expected = "";
    assert_eq!(reverse_string(input), expected);
}

#[test]
fn test_palindrome() {
    let input = "madam";
    let expected = "madam";
    assert_eq!(reverse_string(input), expected);
}