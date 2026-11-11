struct Tour {
	last: u64
}
impl Tour {
	fn first_tour(&self) {
		println!("{}", self.last);
	}
}
fn main() {
	let tour = Tour { last: 5 };
	tour.first_tour();
}
