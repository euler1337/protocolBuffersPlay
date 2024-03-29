extern crate protoc_rust;

use protoc_rust::Customize;

fn main() {
	protoc_rust::run(protoc_rust::Args {
	    out_dir: "src/protos",
	    input: &["../proto/src/addressBook.proto"],
	    includes: &["../proto/src"],
	    customize: Customize {
	      ..Default::default()
	    },
	}).expect("protoc");
}