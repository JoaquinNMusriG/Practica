/*
2) Escribir un programa en lenguaje a elección, que permita:
1. Ingresar el nombre de un archivo con extensión .bmp
2. Valide que el archivo sea con el formato adecuado.
3. Muestre los datos de la cabecera del archivo .bmp
*/

package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
)

func mapToInt(s []byte) int {
	value := 0.0
	for k, v := range s {
		value += float64(v) * math.Pow(2, float64(k*8))
	}
	return int(value)
}

func bmpValidator(s []byte) bool {
	aux := map[int]bool{
		1:  true,
		4:  true,
		8:  true,
		16: true,
		24: true,
	}

	_, ok := aux[mapToInt(s[28:30])]
	firma := s[:2]

	if fmt.Sprintf("%c%c", firma[0], firma[1]) == "BM" &&
		mapToInt(s[26:28]) == 1 &&
		ok &&
		mapToInt(s[34:38])/1024 == mapToInt(s[2:6])/1024 {

		return true
	}

	return false
}

func main() {

	x := ""
	fmt.Printf("Ingresar el nombre del archivo.bmp (sin .bmp):\n")
	fmt.Scanf("%s", &x)
	fmt.Println("Nombre ingresado:", x)

	// leer el arreglo de bytes del archivo
	datosComoBytes, err := ioutil.ReadFile(x + ".bmp")
	if err != nil {
		log.Fatal(err)
	}

	if bmpValidator(datosComoBytes) {
		fmt.Println("Archivo Valido como .BMP")
		fmt.Printf("Primeros dos bytes del archivo: %c\n", datosComoBytes[:2])

		/*Peso del archivo*/
		fmt.Println("Peso del archivo:", mapToInt(datosComoBytes[2:6])/1024)

		/*ancho*/
		//mapToFloat64(datosComoBytes[18:22])
		/*alto*/
		//mapToFloat64(datosComoBytes[22:26])

		fmt.Println("Resolucion:", mapToInt(datosComoBytes[18:22]), "x", mapToInt(datosComoBytes[22:26]))

		/*Planes Sirve para validar 1*/
		fmt.Printf("Planes: %d \n", mapToInt(datosComoBytes[26:28]))

		/*Bits por pixel 1,4,8,16,24*/
		fmt.Printf("Bits por pixel: %d \n", mapToInt(datosComoBytes[28:30]))

		/*Compresión*/
		fmt.Printf("Compresión: %d \n", mapToInt(datosComoBytes[30:34]))

		/*ImagenSize*/
		//fmt.Printf("%d \n", mapToFloat64(datosComoBytes[34:38])/1024)
	} else {
		fmt.Printf("El archivo no es valido.")
	}
}
