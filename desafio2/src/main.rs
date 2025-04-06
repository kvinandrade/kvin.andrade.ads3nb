pub struct Node<T> {
    value: T,
    next: Option<Box<Node<T>>>,
}

pub struct Queue<T> {
    front: Option<Box<Node<T>>>,
    rear: *mut Node<T>,
    size: usize,
}

impl<T> Queue<T> {
    pub fn new() -> Self {
        Self {
            front: None,
            rear: std::ptr::null_mut(),
            size: 0,
        }
    }

    pub fn enqueue(&mut self, value: T) {
        let new_node = Box::new(Node {
            value,
            next: None,
        });
        let raw_node = Box::into_raw(new_node);
        unsafe {
            if self.front.is_none() {
                self.front = Some(Box::from_raw(raw_node));
            } else {
                (*self.rear).next = Some(Box::from_raw(raw_node));
            }
            self.rear = raw_node;
        }
        self.size += 1;
    }

    pub fn dequeue(&mut self) -> Option<T> {
        if let Some(mut front_node) = self.front.take() {
            self.front = front_node.next.take();
            if self.front.is_none() {
                self.rear = std::ptr::null_mut();
            }
            self.size -= 1;
            return Some(front_node.value);
        }
        None
    }

    pub fn peek(&self) -> Option<&T> {
        self.front.as_ref().map(|node| &node.value)
    }

    pub fn size(&self) -> usize {
        self.size
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }
}

fn main() {
    let mut queue = Queue::new();

    queue.enqueue(10);
    queue.enqueue(20);

    println!("Primeiro elemento: {:?}", queue.peek());
    println!("Removido: {:?}", queue.dequeue());
    println!("Tamanho da fila: {}", queue.size());
    println!("Fila está vazia? {}", queue.is_empty());
}