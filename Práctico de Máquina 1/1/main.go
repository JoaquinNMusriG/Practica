package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
)

func validateFile(s []byte) bool {
	if fmt.Sprintf("%c%c%c%c", s[0], s[1], s[2], s[3]) == "RIFF" &&
		fmt.Sprintf("%c%c%c%c", s[8], s[9], s[10], s[11]) == "WAVE" &&
		fmt.Sprintf("%c%c%c", s[12], s[13], s[14]) == "fmt" {
		return true
	}

	return false
}

func mapToInt(s []byte) int {
	value := 0.0
	for k, v := range s {
		value += float64(v) * math.Pow(2, float64(k*8))
	}
	return int(value)
}

func displayDetails(s []byte, dic map[string]field) {
	for k, v := range dic {
		if v.format != "%s" {
			fmt.Printf("%s: "+v.format+"\n", k, mapToInt(s[v.offSSize[0]:v.offSSize[0]+v.offSSize[1]]))
		} else {
			aux := ""
			for i := 0; i < v.offSSize[1]; i++ {
				aux += fmt.Sprintf("%c", s[v.offSSize[0]+i])
			}
			fmt.Printf("%s: "+v.format+"\n", k, aux)
		}
	}
}

type field struct {
	offSSize [2]int
	format   string
}

func main() {
	x := ""
	fmt.Printf("Ingresar el nombre del archivo.bmp (sin .bmp):\n")
	fmt.Scanf("%s", &x)
	fmt.Println("Nombre ingresado:", x)

	dic := map[string]field{
		"ChunkID": {
			format:   "%s",
			offSSize: [2]int{0, 2},
		},
		"ChunkSize": {
			format:   "%d",
			offSSize: [2]int{4, 4},
		},
		"Format": {
			format:   "%s",
			offSSize: [2]int{8, 4},
		},
		"Subchunk1ID": {
			format:   "%s",
			offSSize: [2]int{12, 4},
		},
		"AudioFormat": {
			format:   "%d",
			offSSize: [2]int{20, 2},
		},
		"NumChannels": {
			format:   "%d",
			offSSize: [2]int{22, 2},
		},
		"SampleRate": {
			format:   "%d",
			offSSize: [2]int{24, 4},
		},
		"BitsPerSample": {
			format:   "%d",
			offSSize: [2]int{34, 2},
		},
		"Subchunk2ID": {
			format:   "%s",
			offSSize: [2]int{36, 4},
		},
	}

	datosComoBytes, err := ioutil.ReadFile(x + ".wav")

	if err != nil {
		log.Fatal(err)
	}

	if validateFile(datosComoBytes) {
		fmt.Println("Archivo Valido como .WAV")

		displayDetails(datosComoBytes, dic)

	} else {
		fmt.Printf("El archivo no es valido.")
	}
}
