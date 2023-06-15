import cv2
import os
import string
from time import sleep
from rich.console import Console #for beautiful progress status

#FUNCTIONS
console = Console()

def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

def allign_center(text):
    rows, columns = os.get_terminal_size()
    devided = rows - 1
    return devided

menu_options = {
    1: 'Resize Keduanya',
    2: 'Resize berdasarkan height',
    3: 'Resize berdasarkan width',
    4: 'Exit',
}

def print_menu():

	title = 'Simple Image Resizer '
	print(drawLine('+'))
	print(str.center(title, allign_center(title)))
	print(str.center('github.com/Seftirobim/SimpleImageResizer', allign_center('github.com/Seftirobim/SimpleImageResizer')))
	print(drawLine('+'))
	judul_menu = "Silahkan pilih"

	print(str.center(judul_menu, allign_center(judul_menu)))
	print(drawLine('='))
	for key in menu_options.keys():
		print (key, '--', menu_options[key] )
	print(drawLine('='))

#FUNCTION FOR RESIZE ALL SIZE BASED ON USER INPUT
def scrape_data():
    sleep(0.1)

def resize_images(input_folder, output_folder, size):
    with console.status("[bold green]Memproses gambar...",spinner='aesthetic') as status: #for beautiful progress status

        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                image_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                image = cv2.imread(image_path)
                resized_image = cv2.resize(image, size,fx = 0.75, fy = 0.75)
                cv2.imwrite(output_path, resized_image)
                sleep(0.5)
                console.log(f"[green]Berhasil resize file[/green] {filename}")
                #print(f"{filename} Berhasil di resize")
        console.log(f'[bold][red]Selesai!')

#FUNCTION FOR RESIZE ONLY HEIGHT USER INPUT
def resize_images_height(input_folder, output_folder, height):
    with console.status("[bold green]Memproses gambar...",spinner='aesthetic') as status:
        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                image_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                image = cv2.imread(image_path)
                aspect_ratio = image.shape[1] / image.shape[0]
                width = int(height * aspect_ratio)
                resized_image = cv2.resize(image, (width,height),fx = 0.75, fy = 0.75)
                cv2.imwrite(output_path, resized_image)
                #print(f"{filename} Berhasil di resize")
                sleep(0.5)
                console.log(f"[green]Berhasil resize file[/green] {filename}")
        console.log(f'[bold][red]Selesai!')

#FUNCTION FOR RESIZE ONLY WIDTH USER INPUT
def resize_images_width(input_folder, output_folder, width):
    with console.status("[bold green]Memproses gambar...",spinner='aesthetic') as status:
        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.webp')):
                image_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                image = cv2.imread(image_path)
                aspect_ratio = image.shape[1] / image.shape[0]
                height = int(width / aspect_ratio)
                resized_image = cv2.resize(image, (width, height),fx = 0.75, fy = 0.75)
                cv2.imwrite(output_path, resized_image)
                #print(f"{filename} Berhasil di resize")
                sleep(0.5)
                console.log(f"[green]Berhasil resize file[/green] {filename}")
        console.log(f"[bold][red]Selesai!")

current_folder = os.getcwd()
input_folder = ''.join([current_folder,'/image'])
output_folder = ''.join([current_folder,'/resize'])

#Running Program
while True:
	print_menu()
	option = ''
	try:
		option = int(input('Masukan Option: '))
	except:
		print('Inputan salah. Mohon masukan angka...')
	if option == 1:
		width = int(input("Masukan lebar dalam pixels: "))
		height = int(input("Masukan tinggi dalam pixels: "))
		size = (width, height)
		resize_images(input_folder, output_folder, size)
		break
	elif option == 2:
		height = int(input("Masukan tinggi dalam pixel: ")) 
		resize_images_height(input_folder, output_folder, height)
		break
	elif option == 3:
		width = int(input("Masukan lebar dalam pixel: ")) 
		resize_images_width(input_folder, output_folder, width)
		break
	elif option == 4:
		print ('Terima kasih !') 
		exit()
	else:
		print('Pilihan keliru, silahkan masukan nomor antara 1 - 4')