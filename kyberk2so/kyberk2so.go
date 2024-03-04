package main

// #include <string.h>
import "C"
import (
	kyberk2so "github.com/symbolicsoft/kyber-k2so"
	"unsafe"
)

//export KemKeypair512
func KemKeypair512(sk *C.char, pk *C.char) {
	privKey, pubKey, _ := kyberk2so.KemKeypair512()
	C.memcpy(unsafe.Pointer(sk), unsafe.Pointer(&privKey[0]), C.size_t(len(privKey)))
	C.memcpy(unsafe.Pointer(pk), unsafe.Pointer(&pubKey[0]), C.size_t(len(pubKey)))
}

//export KemEncrypt512
func KemEncrypt512(pk *C.char, ct *C.char, ss *C.char) {
	var publicKey [kyberk2so.Kyber512PKBytes]byte
	C.memcpy(unsafe.Pointer(&publicKey[0]), unsafe.Pointer(pk), C.size_t(len(publicKey)))
	ciphertext, sharedSecret, _ := kyberk2so.KemEncrypt512(publicKey)
	C.memcpy(unsafe.Pointer(ct), unsafe.Pointer(&ciphertext[0]), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

//export KemDecrypt512
func KemDecrypt512(ct *C.char, sk *C.char, ss *C.char) {
	var (
		ciphertext [kyberk2so.Kyber512CTBytes]byte
		privateKey [kyberk2so.Kyber512SKBytes]byte
	)
	C.memcpy(unsafe.Pointer(&ciphertext[0]), unsafe.Pointer(ct), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(&privateKey[0]), unsafe.Pointer(sk), C.size_t(len(privateKey)))
	sharedSecret, _ := kyberk2so.KemDecrypt512(ciphertext, privateKey)
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

//export KemKeypair768
func KemKeypair768(sk *C.char, pk *C.char) {
	privKey, pubKey, _ := kyberk2so.KemKeypair768()
	C.memcpy(unsafe.Pointer(sk), unsafe.Pointer(&privKey[0]), C.size_t(len(privKey)))
	C.memcpy(unsafe.Pointer(pk), unsafe.Pointer(&pubKey[0]), C.size_t(len(pubKey)))
}

//export KemEncrypt768
func KemEncrypt768(pk *C.char, ct *C.char, ss *C.char) {
	var publicKey [kyberk2so.Kyber768PKBytes]byte
	C.memcpy(unsafe.Pointer(&publicKey[0]), unsafe.Pointer(pk), C.size_t(len(publicKey)))
	ciphertext, sharedSecret, _ := kyberk2so.KemEncrypt768(publicKey)
	C.memcpy(unsafe.Pointer(ct), unsafe.Pointer(&ciphertext[0]), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

//export KemDecrypt768
func KemDecrypt768(ct *C.char, sk *C.char, ss *C.char) {
	var (
		ciphertext [kyberk2so.Kyber768CTBytes]byte
		privateKey [kyberk2so.Kyber768SKBytes]byte
	)
	C.memcpy(unsafe.Pointer(&ciphertext[0]), unsafe.Pointer(ct), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(&privateKey[0]), unsafe.Pointer(sk), C.size_t(len(privateKey)))
	sharedSecret, _ := kyberk2so.KemDecrypt768(ciphertext, privateKey)
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

//export KemKeypair1024
func KemKeypair1024(sk *C.char, pk *C.char) {
	privKey, pubKey, _ := kyberk2so.KemKeypair1024()
	C.memcpy(unsafe.Pointer(sk), unsafe.Pointer(&privKey[0]), C.size_t(len(privKey)))
	C.memcpy(unsafe.Pointer(pk), unsafe.Pointer(&pubKey[0]), C.size_t(len(pubKey)))
}

//export KemEncrypt1024
func KemEncrypt1024(pk *C.char, ct *C.char, ss *C.char) {
	var publicKey [kyberk2so.Kyber1024PKBytes]byte
	C.memcpy(unsafe.Pointer(&publicKey[0]), unsafe.Pointer(pk), C.size_t(len(publicKey)))
	ciphertext, sharedSecret, _ := kyberk2so.KemEncrypt1024(publicKey)
	C.memcpy(unsafe.Pointer(ct), unsafe.Pointer(&ciphertext[0]), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

//export KemDecrypt1024
func KemDecrypt1024(ct *C.char, sk *C.char, ss *C.char) {
	var (
		ciphertext [kyberk2so.Kyber1024CTBytes]byte
		privateKey [kyberk2so.Kyber1024SKBytes]byte
	)
	C.memcpy(unsafe.Pointer(&ciphertext[0]), unsafe.Pointer(ct), C.size_t(len(ciphertext)))
	C.memcpy(unsafe.Pointer(&privateKey[0]), unsafe.Pointer(sk), C.size_t(len(privateKey)))
	sharedSecret, _ := kyberk2so.KemDecrypt1024(ciphertext, privateKey)
	C.memcpy(unsafe.Pointer(ss), unsafe.Pointer(&sharedSecret[0]), C.size_t(len(sharedSecret)))
}

func main() {}
