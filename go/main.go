package main

import (
	"fmt"
	"net"

	"github.com/libp2p/go-libp2p"
)

func handleConnection(conn net.Conn) {
	// Bağlantıdan gelen veriyi oku
	buffer := make([]byte, 1024)
	n, _ := conn.Read(buffer)
	receivedData := string(buffer[:n])
	fmt.Println("Received:", receivedData)

	// Gelen görevi işleme
	var response string
	if receivedData == "compute_task" {
		// Örnek bir işlem yapın
		result := 42 // Örnek sonuç
		response = fmt.Sprintf("Computed result: %d", result)
	} else {
		response = "Unknown task"
	}

	// Yanıtı gönder
	conn.Write([]byte(response))
	conn.Close()
}

func main() {
	// libp2p düğümünü başlat
	node, err := libp2p.New()
	if err != nil {
		panic(err)
	}
	fmt.Println("Libp2p node started: ", node.ID())

	// TCP sunucusu başlat
	listener, err := net.Listen("tcp", ":9000")
	if err != nil {
		panic(err)
	}
	fmt.Println("Listening on port 9000")

	// Bağlantıları kabul et
	for {
		conn, _ := listener.Accept()
		go handleConnection(conn)
	}
}
