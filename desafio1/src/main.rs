pub fn reverse_string(input: &str) -> String {
    input.chars().rev().collect()
}

fn main() {
    let original = "abc";
    let reversed = reverse_string(original);

    println!("Original: {}", original);
    println!("Invertido: {}", reversed);
}
