package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)



func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", HomeHandler)
    http.Handle("/", r)
}